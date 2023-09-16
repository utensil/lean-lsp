# lean-lsp

Lean 4 language server wrapper for [Jupyter LSP](https://jupyterlab-lsp.readthedocs.io/en/latest/), making it possible to write/run Lean 4 in JupyterLab, utilizing the [Lean 4 Language Server implemented in Lean 4 itself](https://github.com/leanprover/lean4/tree/master/src/Lean/Server).

## Installation

1. Ensure you have a working Lean 4 installation, see [the Lean 4 installation instructions](https://leanprover-community.github.io/get_started.html).

2. Install lean-lsp and its dependencies via `pip`:

```bash
pip install 'jupyterlab>=4.0.0,<5.0.0a0'
# pip install jupyterlab-lsp==5.0.0b1
pip install git+https://github.com/utensil/jupyterlab-lsp.git@main#subdirectory=python_packages/jupyter_lsp
pip install git+https://github.com/utensil/lean-lsp.git
```

3. Ensure you have a working Lean 4 project, see [Lean projects](https://leanprover-community.github.io/install/project.html).

4. Start JupyterLab **from the root of a Lean 4 project** and choose the Lean 4 Langauge Server:

```
ln -s / .lsp_symlink
jupyter server extension enable --sys-prefix --py jupyter_lsp
jupyter lab --ContentsManager.allow_hidden=True
```

TODO: step 4 is not working yet.

5. Have fun!

## Development

Just run `pip -e .` instead of `pip install git+https://github.com/utensil/lean-lsp.git` above.