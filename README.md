# cole_press

This is a website published with Quarto and Netlify. It can be found [here](https://cole.press).

## Setup

Run `./setup.sh` to install R and Quarto before building the site:

```bash
./setup.sh
```

## Local development

After installing the required tools, you can preview or render the site using
Quarto. These commands are useful for testing changes locally before pushing
them to the live site.

To start a local preview server that rebuilds the site as you edit files, run:

```bash
quarto preview
```

If you just want to generate the static HTML output without launching the
preview server, you can render the site instead:

```bash
quarto render
```
