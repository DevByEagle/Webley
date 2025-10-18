---
icon: material/download-outline
---

Installing Webley is straightforward and requires minimal setup. It runs on Python 3.10+ without any extra configuration.

## Installing via PyPI <small>Recommended</small> {#pypi data-toc-label="PyPI"}

The easiest way to install Webley is through **PyPI**. It’s a one-line command with no additional downloads required.

1. Open your terminal or command prompt.

2. Run the installation command:

    ```bash
    pip install webley
    ```

3. Verify the installation:

    ```bash
    python -c "import webley; print('Webley version:', webley.__version__)"
    ```

!!! tip
    To keep your project dependencies isolated, consider using a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # macOS/Linux
    env\Scripts\activate     # Windows
    pip install webley
    ```

## Installing from GitHub <small>Development Version</small> {#github data-toc-label="GitHub"}

For the **latest features** or if you plan to **contribute to Webley**, you can install directly from GitHub. This gives you access to updates before they are released on PyPI.

1. Clone the repository:

    ```bash
    git clone https://github.com/DevByEagle/Webley.git
    cd Webley
    ```

2. Install Webley:

    ```bash
    pip install .
    ```

3. Verify the installation:

    ```bash
    python -c "import webley; print('Webley version:', webley.__version__)"
    ```

!!! info
    Installing from GitHub is ideal for testing cutting-edge features. For most users, **PyPI** remains the recommended option.