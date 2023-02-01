# JellyMl

JellyML is an open-source tool (python API and command line) for effortlessly embedding a snapshot of your code 
             | into a checkpoint of a pytorch model.
Learn more at [jellyml.com](jellyml.com)

## Structure of the jellyml repository
(Note that the jellyml repository is a monorepo. If you are
reading this from the python package source code,
go to github.com/mmulet/jellyml to see the whole repository)

- jellyml is the source for the python package
- jellyml-lightning is the source for pytorch lightning plugin
- client is the source for the website
- dev_server is the source for the development server of the website

## Build

### jellyml

1. Make a venv
```sh
python3 -m venv venv
# activate the venv ( depends on your shell and OS)
# see https://docs.python.org/3/library/venv.html
# bash
source venv/bin/activate
```
2. Install build
```sh
pip install build
```
3.  Build the package
```sh
cd jellyml
python -m build
pip install dist/jellyml-0.0.1-py3-none-any.whl
```

### jellyml-lightning
1. Follow the directions for building and installing jellyml.
   jellyml is a dependency of jellyml-lightning.
2. Build the package
```sh
cd jellyml-lightning
python -m build
pip install dist/jellyml-lightning-0.0.1-py3-none-any.whl
```

### Website

#### Build the website

```sh
cd client
npm install .
cd ../dev_server
npm install .
npm run build
```

#### Dev the website

```sh
cd client
npm install .
cd ../dev_server
npm install .
npm run build
```

## Tests

Located in the source files in src/jellyml. Have the prefix test\_.
Run them as a module

```sh
cd src;
python3 -m jellyml.test_all
```
