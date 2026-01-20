# Translation Library I18N File Standards

This directory contains example I18N TOML files for your reference. These examples are named in compliance with ISO 639-1 (language code).

### File naming

#### Consistency

You are free to name your files as you wish, as long as the file naming is consistent.
Make sure that your `config.toml` is up-to-date with any file name changes.

#### Standards

While the most common standard seems to be `BCP 47`, depending on your use case, you may want to name your I18N files differently. Here are some examples:

| Standard    | Description        | Examples                                             |
| ----------- | ------------------ | ---------------------------------------------------- |
| `ISO 639-1` | language (2 chars) | (`en`, `de`, `ja`, etc. )                            |
| `ISO 3166`  | region             | (`US`, `GB`, `DE`, `AT`, `JP`, etc.)                 |
| `BCP 47`    | language + region  | (`en-US`, `en-GB`, `de-DE`, `de-AT`, `ja-JP`, etc. ) |
