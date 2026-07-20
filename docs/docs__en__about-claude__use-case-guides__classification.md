# Classification

Claude excels at processing, understanding, and recognizing patterns in text, images, and data. These capabilities make Claude especially powerful for classification tasks. 

---

This guide walks through the process of determining the best approach for building a classifier with Claude and the essentials of end-to-end deployment for a Claude classifier, from use case exploration to back-end integration. <Tip>
  Visit the&#x20;

  [classification cookbooks](https://platform.claude.com/cookbook/capabilities-classification-guide)

  &#x20;to see example classification implementations using Claude.
</Tip>

## When to use Claude for classification

When should you consider using an LLM instead of a traditional ML approach for your classification tasks? Here are some key indicators:

1. **Rule-based classes**: Use Claude when classes are defined by conditions rather than examples, as it can understand underlying rules.
2. **Evolving classes**: Claude adapts well to new or changing domains with emerging classes and shifting boundaries.
3. **Unstructured inputs**: Claude can handle large volumes of unstructured text inputs of varying lengths.
4. **Limited labeled examples**: With few-shot learning capabilities, Claude learns accurately from limited labeled training data.
5. **Reasoning Requirements**: Claude excels at classification tasks requiring semantic understanding, context, and higher-level reasoning.

***

## Establish your classification use case

Below is a non-exhaustive list of common classification use cases where Claude excels by industry.

<AccordionGroup>
  <Accordion title="Tech & IT">
    * **Content moderation**: automatically identify and flag inappropriate, offensive, or harmful content in user-generated text, images, or videos.
    * **Bug prioritization**: classify software bug reports based on their severity, impact, or complexity to prioritize development efforts and allocate resources effectively.
  </Accordion>

  <Accordion title="Customer Service">
    * **Intent analysis**: determine what the user wants to achieve or what action they want the system to perform based on their text inputs.
    * **Support ticket routing**: analyze customer interactions, such as call center transcripts or support tickets, to route issues to the appropriate teams, prioritize critical cases, and identify recurring problems for proactive resolution.
  </Accordion>

  <Accordion title="Healthcare">
    * **Patient triaging**: classify customer intake conversations and data according to the urgency, topic, or required expertise for efficient triaging.
    * **Clinical trial screening**: analyze patient data and medical records to identify and categorize eligible participants based on specified inclusion and exclusion criteria.
  </Accordion>

  <Accordion title="Finance">
    * **Fraud detection**: identify suspicious patterns or anomalies in financial transactions, insurance claims, or user behavior to prevent and mitigate fraudulent activities.
    * **Credit risk assessment**: classify loan applicants based on their creditworthiness into risk categories to automate credit decisions and optimize lending processes.
  </Accordion>

  <Accordion title="Legal">
    * **Legal document categorization**: classify legal documents, such as pleadings, motions, briefs, or memoranda, based on their document type, purpose, or relevance to specific cases or clients.
  </Accordion>
</AccordionGroup>

***

## Implement Claude for classification

The three key model decision factors are: intelligence, latency, and price.

For classification, a smaller model like Claude Haiku 4.5 is typically ideal due to its speed and efficiency. Though, for classification tasks where specialized knowledge or complex reasoning is required, Sonnet or Opus may be a better choice. Learn more about how Opus, Sonnet, and Haiku compare in the [models overview](/docs/en/about-claude/models).

Use evaluations to gauge whether a Claude model is performing well enough to launch into production.

### 1. Build a strong input prompt

While Claude offers high-level baseline performance out of the box, a strong input prompt helps get the best results.

For a generic classifier that you can adapt to your specific use case, copy the starter prompt below:

<Accordion title="Starter prompt">
  ```text wrap
  You will be building a text classifier that can automatically categorize text into a set of predefined categories.
  Here are the categories the classifier will use:

  <categories>
  {{CATEGORIES}}
  </categories>

  To help you understand how to classify text into these categories, here are some example texts that have already been labeled with their correct category:

  <examples>
  {{EXAMPLES}}
  </examples>

  Please carefully study these examples to identify the key features and characteristics that define each category. Write out your analysis of each category inside <category_analysis> tags, explaining the main topics, themes, writing styles, etc. that seem to be associated with each one.

  Once you feel you have a good grasp of the categories, your task is to build a classifier that can take in new, unlabeled texts and output a prediction of which category it most likely belongs to.

  Before giving your final classification, show your step-by-step process and reasoning inside <classification_process> tags. Weigh the evidence for each potential category.

  Then output your final <classification> for which category you think the example text belongs to.

  The goal is to build a classifier that can accurately categorize new texts into the most appropriate category, as defined by the examples.
  ```
</Accordion>

### 2. Develop your test cases

To run your classification evaluation, you will need test cases to run it on. Take a look at the guide to [developing test cases](/docs/en/test-and-evaluate/develop-tests).

### 3. Run your eval

#### Evaluation metrics

Some success metrics to consider evaluating Claude’s performance on a classification task include:

| Criteria              | Description                                                                                                                                                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Accuracy**          | The model's output exactly matches the golden answer or correctly classifies the input according to the task's requirements. This is typically calculated as (Number of correct predictions) / (Overall number of predictions). |
| **F1 Score**          | The model's output optimally balances precision and recall.                                                                                                                                                                     |
| **Consistency**       | The model's output is consistent with its predictions for similar inputs or follows a logical pattern.                                                                                                                          |
| **Structure**         | The model's output follows the expected format or structure, making it easy to parse and interpret. For example, many classifiers are expected to output JSON format.                                                           |
| **Speed**             | The model provides a response within the acceptable time limit or latency threshold for the task.                                                                                                                               |
| **Bias and Fairness** | If classifying data about people, is it important that the model does not demonstrate any biases based on gender, ethnicity, or other characteristics that would lead to its misclassification.                                 |

## Deploy your classifier

To see code examples of how to use Claude for classification, check out the [Classification Guide](https://platform.claude.com/cookbook/capabilities-classification-guide) in the Claude Cookbook.
