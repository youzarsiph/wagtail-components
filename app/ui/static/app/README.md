# UI Styles

Basic commands to get started.

First `cd` into dir:

```console
cd app/ui/static/ui
```

To generate the styles:

```console
npm install
cd app/ui/static/app
npx @tailwindcss/cli -i ../static/app/css/app.css -o ../static/app/css/styles.css --cwd ../../templates -m -w
```

To format the templates:

```console
npx prettier -w ../../templates
```
