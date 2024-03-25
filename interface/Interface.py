# %%
from abc import ABC, abstractmethod

from core.AtivosCore import Ativos

from backend.firebase import firestore


class InterfaceAtivos(ABC):
    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def save(self, ativo: Ativos):
        pass


class CollectionAtivos(InterfaceAtivos):
    def read(self, id):
        docRef = firestore.collection("ativos").document(id)
        docSnap = docRef.get()
        if docSnap.exists:
            ret = docSnap.to_dict()
            ret["id"] = docSnap.id
            return Ativos.from_dict(ret)
        else:
            return Ativos.vazio()

    def save(self, ativo: Ativos):
        if ativo.id:
            # tem id = update
            docRef = firestore.collection("ativos").document(ativo.id)
            docRef.update(ativo)
            return ativo
        else:
            # não tem id = criar
            return firestore.collection("ativos").add(ativo.to_dict())[1].id

    def collection():
        return firestore.collection("ativos")


# %%
