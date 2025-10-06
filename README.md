# wagtail-components

[![CI](https://github.com/youzarsiph/wagtail-components/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/wagtail-components/actions/workflows/ci.yml)
[![CD](https://github.com/youzarsiph/wagtail-components/actions/workflows/cd.yml/badge.svg)](https://github.com/youzarsiph/wagtail-components/actions/workflows/cd.yml)
[![Code Style: Black](https://github.com/youzarsiph/wagtail-components/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/wagtail-components/actions/workflows/black.yml)
[![Code Linting: Ruff](https://github.com/youzarsiph/wagtail-components/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/wagtail-components/actions/workflows/ruff.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/wagtail-components?logo=pypi&logoColor=white)](https://pypi.org/project/wagtail-components/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/wagtail-components?logo=python&logoColor=white)](https://pypi.org/project/wagtail-components/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/wagtail-components?logo=pypi&logoColor=white)](https://pypi.org/project/wagtail-components/)
[![PyPI - License](https://img.shields.io/pypi/l/wagtail-components?logo=pypi&logoColor=white)](https://pypi.org/project/wagtail-components/)

---

## Overview

**Wagtail Components** is a Django + Wagtail package that helps you build websites faster with clean, reusable building blocks. It ships with ready‑to‑use templates, utilities, and UI components styled with **Tailwind CSS** and **daisyUI**, so you can focus on content and design instead of boilerplate.

---

## Included Templates

- **Breadcrumbs** – show users where they are in the site hierarchy.
- **Forms** – styled forms with validation.
- **Messages** – display Django system messages.
- **Pagination** – navigate paginated content.
- **Prev/Next Navigation** – simple previous/next links.
- **Page Title** – recursive page title rendering.
- **Tree** – recursive menu rendering.

---

## Key Features

- **CI/CD Pipelines** – automated with GitHub Actions for reliable deployments.
- **Dependency Management** – powered by Poetry for clean, reproducible builds.
- **Code Formatting** – enforced with Black for consistency.
- **Linting** – Ruff integration to catch issues early.
- **Configuration** – sensible defaults with `.gitignore`, `pyproject.toml`, and more.

---

## Quick Start

Install the package:

```bash
pip install wagtail-components
```

Add it to your project:

```python
# settings.py
INSTALLED_APPS = [
    "wagtail_components",
    ...
]
```

Use the components in your templates (requires a Wagtail `Page` instance in context):

```html
{% load docs i18n static wagtailcore_tags %}

<!DOCTYPE html>
<html>
  <!-- You need to implement this tag -->
  {% get_site_root as home %}
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- Recursive titles -->
    <title>
      {% trans 'WC Example' %} | {% include 'wagtail/components/title.html' %}
    </title>
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
  </head>
  <body class="antialiased">
    <div class="drawer lg:drawer-open">
      <input id="nav-drawer" type="checkbox" class="drawer-toggle" />
      <section class="drawer-content">
        <div class="relative h-dvh overflow-hidden">
          <section class="bg-base-100 relative size-full grow overflow-hidden">
            <section class="size-full grid gap-4 overflow-y-auto">
              <header class="absolute inset-x-0 top-0 z-40 backdrop-blur-3xl">
                <nav class="navbar p-4">
                  <ol class="navbar-start gap-4">
                    <li
                      class="tooltip tooltip-right tooltip-primary z-10 lg:hidden"
                      data-tip="{% trans 'Open drawer' %}"
                    >
                      <label
                        for="nav-drawer"
                        aria-label="{% trans 'close sidebar' %}"
                        class="btn btn-square btn-soft btn-sm btn-primary md:btn-md 2xl:btn-lg"
                      >
                        <i data-lucide="menu" class="size-4 md:size-6"></i>
                        <span class="sr-only">{% trans 'Open drawer' %}</span>
                      </label>
                    </li>
                    <li
                      class="tooltip tooltip-right tooltip-primary"
                      data-tip="{% trans 'Wagtail Components Demo' %}"
                    >
                      <h1 class="relative">
                        <a href="{% pageurl home %}">{% trans 'WC Demo' %}</a>
                      </h1>
                    </li>
                  </ol>
                </nav>
              </header>

              <!-- Messages -->
              {% include 'wagtail/components/messages.html' %}

              <div class="container flex flex-col gap-8 px-4 py-20 mx-auto">
                <!-- Breadcrumbs -->
                {% include 'wagtail/components/breadcrumbs.html' %}
                <div class="mx-auto prose prose-sm xl:prose-lg 2xl:prose-xl">
                  <h1>{{ page.title }}</h1>
                  <div>{{ page.content }}</div>
                  
                  <div class="not-prose">
                    <!-- Styled forms with validation -->
                    {% include 'wagtail/components/from.html' %}
                  </div>
                </div>
                <!-- Prev/Next nav -->
                {% include 'wagtail/components/prev_next.html' %}
              </div>
            </section>
          </section>
        </div>
      </section>
      <section class="drawer-side z-50">
        <label for="nav-drawer" class="drawer-overlay"></label>
        <section class="bg-base-100 flex size-full flex-col overflow-y-auto">
          <div class="grid">
            <header class="flex items-center justify-between gap-4">
              <div
                class="tooltip tooltip-right tooltip-primary tooltip-open aspect-square"
                data-tip="{% trans 'Wagtail Component Demo' %}"
              >
                <h1 class="relative">
                  <a
                    href="{% pageurl home %}"
                    class="btn btn-square btn-primary lg:btn-lg"
                  >
                    {% trans 'WC Demo' %}
                  </a>
                </h1>
              </div>
              <div
                class="tooltip tooltip-left hover:tooltip-error lg:hidden"
                data-tip="{% trans 'Close' %}"
              >
                <label
                  for="nav-drawer"
                  aria-label="{% trans 'close sidebar' %}"
                  class="btn btn-square btn-soft btn-sm btn-primary hover:btn-error md:btn-md 2xl:btn-lg"
                >
                  <i data-lucide="x" class="size-4 md:size-6"></i>
                  <span class="sr-only">{% trans 'Close' %}</span>
                </label>
              </div>
            </header>
            <ul class="menu 2xl:menu-lg size-full grow gap-2">
              <!-- Recursive menu rendering with collapsible menus -->
              {% include 'wagtail/components/tree.html' with nodes=home.get_children %}
            </ul>
          </div>
        </section>
      </section>
    </div>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script>lucide.createIcons()</script>
  </body>
</html>
```

---

## Contributing

Contributions are welcome! Please see our [CONTRIBUTING](CONTRIBUTING.md) guide for details. Feedback, issues, and pull requests all help improve the project.

---

## Support

For questions or support, open an issue or join the conversation in [GitHub Discussions](https://github.com/youzarsiph/wagtail-components/discussions).

---

## License

Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
