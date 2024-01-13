[Install Hugo](https://gohugo.io/installation/macos/#homebrew)

```sh
brew install hugo
```

# Congo


[Install using git](https://jpanther.github.io/congo/docs/installation/#install-using-git)

```sh
git submodule add -b stable https://github.com/jpanther/congo.git themes/congo
```

[Update using git](https://jpanther.github.io/congo/docs/installation/#update-using-git)

```sh
git submodule update --remote --merge
```

Once you've done the prerequisite:

- [`config/_default`](https://jpanther.github.io/congo/docs/installation/#set-up-theme-configuration-files)
    ```
    config/_default/
    ├─ config.toml
    ├─ markup.toml
    ├─ menus.toml
    ├─ module.toml  # if you installed using Hugo Modules
    └─ params.toml
    ```

- [Directory structure](https://jpanther.github.io/congo/docs/getting-started/#directory-structure)
    ```
    .
    ├── assets
    │   └── img
    │       └── author.jpg
    ├── config
    │   └── _default
    ├── content
    │   ├── _index.md
    │   ├── about.md
    │   └── posts
    │       ├── _index.md
    │       ├── first-post.md
    │       └── another-post
    │           ├── aardvark.jpg
    │           └── index.md
    └── themes
        └── congo
    ```
- [Project structure](https://jpanther.github.io/congo/docs/advanced-customisation/#project-structure)
    ```
    .
    ├── assets
    │   └── css
    │       └── compiled
    │           └── main.css  # this is the file we will generate
    ├── config  # site config
    │   └── _default
    ├── content  # site content
    │   ├── _index.md
    │   ├── projects
    │   │   └── _index.md
    │   └── blog
    │       └── _index.md
    ├── layouts  # custom layouts for your site
    │   ├── partials
    │   │   └── extend-article-link.html
    │   ├── projects
    │   │   └── list.html
    │   └── shortcodes
    │       └── disclaimer.html
    └── themes
        └── congo  # git submodule or manual theme install
    ```

# Blowfish

[Install using git](https://blowfish.page/docs/installation/#install-using-git)

```sh
git submodule add -b main https://github.com/nunocoracao/blowfish.git themes/blowfish
```

[Update using git](https://blowfish.page/docs/installation/#update-using-git)

```sh
git submodule update --remote --merge
```
