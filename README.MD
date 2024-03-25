# CLEAN ARCHITECTURE EXAMPLE IN PYTHON

## Summary

Simple example of how to define a neat structure based on <a href="https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html" target="_blank">Uncle Bob's Clean Architecture</a>.

### This app:

Download data from Public Companies on CVM's open database (<a href="https://dados.cvm.gov.br/" target="_blank">Portal Dados Abertos CVM</a>) and save it on Firebase (<a href="https://firebase.google.com/" target="_blank">see here</a>).

### Structure:

Main file: `main.py`

Here we define the Core of the application: `/core/AtivosCore.py`

Here we define what we want to do with each entity: `/interface/Interface.py`

- first we define the Abstract methods (`class InterfaceAtivos(ABC)`);
- then we integrate with Firebase as our backend (`class CollectionAtivos(InterfaceAtivos)`) as a implementation of the Abstract methods.

On `/backend/firebase.py`: we define/start our backend.

## Important!

Check the .gitignore file and use it too!

> Don't expose **_sensitive information_** to the public!

Also:

1. Check the `requirements.txt`;
2. Use a virtual enviroment (`python -m venv /path-to-venv`);
3. To use the same packages as I did, after creating the `venv`:

- `path-to-venv/Scripts/activate`
- `pip install -r <path-to-requirements.txt>`

> **Notebook**: I use VS Code and its "native" notebook (Interactive). That's why you'll see `#%%` on some .py files, `#%%` creates a cell and I can run it on a Interactive window. It needs somethings installed in your vscode, but it's very easy to set it up.

## Benefits of this structure

- Core is independent from outside layers: if we save the data on Excel or MySQL DB, our core **NEVER** changes
- Interface layer defines what we want to do with the entities -- easy to understand what we want to do
- Collection layer connects the Interface abstract methods with our backend -- hands on! Do whatever we want...
- Change the services with ease: if Firebase is no longer suited for our needs, we only have to change the /backend layer and the /collections layer, no change in our core (because it only changes if the BUSINESS changed first)
- Core = BUSINESS tells what it needs to be, not the technology

## Licence

Feel free to use it as an example or change however you like...

Comments are very welcomed!
