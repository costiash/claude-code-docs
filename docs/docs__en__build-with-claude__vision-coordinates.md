# Coordinates and bounding boxes

How Claude resizes images, and how to work with the pixel coordinates it returns for bounding boxes, points, and UI elements.

---

Claude can locate and label regions of an image (for example, returning bounding boxes for tables, form fields, chart elements, or UI components). This guide covers how Claude resizes images before processing them and how to work with the pixel coordinates it returns, so that boxes and points line up with your original image.

You'll need this for OCR pipelines, form extraction, chart parsing, UI element location, and any task where you act on a specific region of an image. For sending images, supported formats, and per-model resolution limits, see [Vision](/docs/en/build-with-claude/vision).

<Note>
  **Claude works best with absolute pixel coordinates.** Ask for them explicitly in your prompt. For example: *"Return the bounding box of each table as `[x1, y1, x2, y2]` in pixel coordinates."* Claude does not work well when you ask for normalized coordinates, for example: *"Return bounding box coordinates between `0` and `1000`."* Always ask for pixel coordinates and normalize in your own code if you need to.
</Note>

Coordinates follow the standard image convention: the origin `(0, 0)` is the top-left corner of the image, with x increasing to the right and y increasing downward. The coordinates Claude returns are pixel positions in the image Claude sees: your image after Claude resizes it to fit the model's native resolution (see [How Claude resizes and pads images](#how-claude-resizes-and-pads-images)). To get coordinates you can use directly, either pre-resize your image so the coordinates map one-to-one onto the image you have (see [Resize your image before uploading](#resize-your-image-before-uploading)), or rescale the coordinates Claude returns (see [Rescale coordinates when you cannot pre-resize](#rescale-coordinates-when-you-cannot-pre-resize)).

<Note>
  Claude's spatial reasoning has limits (see [Limitations](/docs/en/build-with-claude/vision#limitations)). Coordinate accuracy is best when you state the expected coordinate format in your prompt and spot-check results visually before processing at scale. For [PDF support](/docs/en/build-with-claude/pdf-support), pages are rasterized to images server-side at dimensions you don't control, so the returned coordinates can't be reliably mapped back onto the page. To work with coordinates on PDF content, rasterize the pages to images yourself and use the pre-resize approach.
</Note>

## How Claude resizes and pads images

Claude finds the largest aspect-preserving size that satisfies both of the model's image limits:

1. **Edge limit:** neither side exceeds the maximum edge length (1568 px on the standard tier, 2576 px on the high-resolution tier).
2. **Visual token limit:** the image's token cost `⌈width / 28⌉ × ⌈height / 28⌉` does not exceed the model's visual token budget (1568 tokens on the standard tier, 4784 on the high-resolution tier).

See [Resolution and token cost](/docs/en/build-with-claude/vision#evaluate-image-size) for which models are in which tier.

For most photos and screenshots the edge limit is what triggers a resize. For portrait documents the visual token limit usually triggers first, and overlooking it is the most common cause of misaligned coordinates. For example, an A4 page scanned at 130 DPI is 1075×1520 pixels: both sides are under 1568 px, but it costs `39 × 55 = 2145` visual tokens, so Claude resizes it to 924×1307.

Claude then pads every image, resized or not, up to the next multiple of 28 pixels on the bottom and right edges (924×1307 becomes 924×1316 in the example). The padding contains no content: Claude perceives the padded image, but the page content only ever occupies the un-padded resized region. **Always normalize or rescale by the resized dimensions, not the padded dimensions**; dividing by the padded dimensions scales every coordinate by a small amount.

## Resize your image before uploading

The most reliable approach is to resize your image yourself before uploading, so the image you have is exactly the image Claude sees and the coordinates Claude returns need no conversion.

The following reference implementation computes the exact size Claude resizes an image to:

```python
import math


def count_image_tokens(width: int, height: int) -> int:
    """Visual tokens consumed by an image: one token per 28x28 pixel patch."""
    return math.ceil(width / 28) * math.ceil(height / 28)


def resized_size(
    width: int,
    height: int,
    max_edge: int = 1568,
    max_tokens: int = 1568,
) -> tuple[int, int]:
    """The size Claude resizes an image to before padding.

    Defaults are for the standard resolution tier. For high-resolution-tier
    models, use max_edge=2576 and max_tokens=4784. Returns (width, height).
    Images that already fit within the limits are returned unchanged.
    """

    def fits(w: int, h: int) -> bool:
        return (
            math.ceil(w / 28) * 28 <= max_edge
            and math.ceil(h / 28) * 28 <= max_edge
            and count_image_tokens(w, h) <= max_tokens
        )

    if fits(width, height):
        return (width, height)
    if height > width:
        resized_h, resized_w = resized_size(height, width, max_edge, max_tokens)
        return (resized_w, resized_h)

    # Binary search along the long edge for the largest aspect-preserving
    # size that fits.
    aspect_ratio = width / height
    lo, hi = 1, width  # lo always fits; hi never fits
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if fits(mid, max(round(mid / aspect_ratio), 1)):
            lo = mid
        else:
            hi = mid
    return (lo, max(round(lo / aspect_ratio), 1))


# The A4 example from "How Claude resizes and pads images":
print(resized_size(1075, 1520))  # (924, 1307)
```

1. Resize the image to the dimensions returned by `resized_size`. If the image already fits within the model's limits, `resized_size` returns its dimensions unchanged and no resize is needed.
2. Send the resized image to the API. Don't pad it yourself; Claude handles padding, and padding doesn't shift the coordinate origin.
3. In your prompt, ask explicitly for pixel coordinates. For example: *"Return the bounding box of each table as `[x1, y1, x2, y2]` in pixel coordinates."*
4. Use the returned coordinates directly against the image you sent. If you need normalized coordinates, divide by the dimensions of the image you sent, not by the original image's dimensions and not by the padded dimensions.

## Rescale coordinates when you cannot pre-resize

If you cannot pre-resize (for example, when the image comes from an upstream system you can't modify), use `resized_size` from [Resize your image before uploading](#resize-your-image-before-uploading) to recover the dimensions Claude saw, then map the coordinates Claude returns into normalized coordinates or back onto your original image. This approach requires knowing the pixel dimensions of the image you uploaded, so it does not apply to PDF uploads.

```python
def to_relative_coordinates(
    x: float,
    y: float,
    original_width: int,
    original_height: int,
    max_edge: int = 1568,
    max_tokens: int = 1568,
) -> tuple[float, float]:
    """Map a pixel coordinate returned by Claude to relative coordinates in [0, 1].

    Pass the dimensions of the image you uploaded. For high-resolution-tier
    models, use max_edge=2576 and max_tokens=4784.
    """
    resized_w, resized_h = resized_size(
        original_width, original_height, max_edge, max_tokens
    )
    return (x / resized_w, y / resized_h)


# To express the coordinate in your original image's pixel space, multiply the
# relative coordinate by your original dimensions:
# (rel_x * original_width, rel_y * original_height)
```

Padding is applied only to the bottom and right edges, so the origin doesn't shift and a per-axis linear rescale is sufficient.

## Related

* The [Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool) requires screenshots to already fit within image size limits (oversized screenshots are rejected, not resized); see its scaling guidance for the client-side resize and coordinate-scaling pattern.
* [PDF support](/docs/en/build-with-claude/pdf-support): pages are rasterized server-side at dimensions you don't control, so rasterize pages yourself and use the pre-resize approach when you need coordinates on PDF content.
