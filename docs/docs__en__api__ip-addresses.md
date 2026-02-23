# IP addresses

Anthropic services use fixed IP addresses for both inbound and outbound connections. You can use these addresses to configure your firewall rules for secure access to the Claude API and Console. These addresses will not change without notice.

---

## Inbound IP addresses

These are the IP addresses where Anthropic services receive incoming connections.

### IPv4

`160.79.104.0/23`

### IPv6

`2607:6bc0::/48`

## Outbound IP addresses

These are the stable IP addresses that Anthropic uses for outbound requests (for example, when making MCP tool calls to external servers).

### IPv4

`160.79.104.0/21`

### Phased out IP addresses

The following IP addresses are no longer in use by Anthropic. If you have previously allowlisted these addresses, you should remove them from your firewall rules.

```text
34.162.46.92/32
34.162.102.82/32
34.162.136.91/32
34.162.142.92/32
34.162.183.95/32
```