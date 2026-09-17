# Field-level evidence

The survey treats provenance as part of the extracted data, not as a separate note added later.

A field-level evidence object records:

- the record and field identifiers,
- source URL,
- snapshot/content hash,
- retrieval time,
- a structural or visual locator,
- the supporting text or attribute value,
- the extracted value,
- the normalized value,
- and the transformation history.

The machine-readable definition is `schemas/evidence-object.schema.json`.

For the wireless-headphones experiment, the contract is stricter. Every non-null field must provide both CSS and XPath locators plus an exact supporting quote. CSS and XPath must point to the same DOM node. The evaluator also checks that the node belongs to the aligned product card and that the quoted source really supports the predicted value.

The experiment files are under `IJDSA_experiment/`.
