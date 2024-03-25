# %%
import glob
import requests
import os
import zipfile
from datetime import datetime
from dotenv import load_dotenv

import pandas as pd

CWD = os.getcwd()
SAVE_RAW = f"{CWD}\\dados_cvm"

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_env = load_dotenv(dotenv_path)


# %%
def download_data() -> None:
    os.chdir(SAVE_RAW)
    ANOS = range(2010, 2024)
    LINK_RAIZ = (
        "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_{}.zip"
    )

    for ano in ANOS:
        print(f"downloading now: {ano}")
        download = requests.get(LINK_RAIZ.format(ano))
        open(f"dfp_cia_aberta_{ano}.zip", "wb").write(download.content)


# %%
def concat_data() -> None:
    list_demonstracoes = []
    for arquivo in glob.glob("*.zip"):
        print(arquivo)
        arq_zip = zipfile.ZipFile(arquivo)
        # arq_zip = zipfile.ZipFile("dfp_cia_aberta_2010.zip")
        cols = []
        for planilha in arq_zip.namelist():
            # planilha = "dfp_cia_aberta_2010.csv"
            # print(planilha)
            date_cols_1 = ["DT_REFER", "DT_INI_EXERC", "DT_FIM_EXERC"]
            date_cols_2 = ["DT_REFER", "DT_FIM_EXERC"]

            try:
                dfp = pd.read_csv(
                    arq_zip.open(planilha),
                    sep=";",
                    encoding="iso-8859-1",
                    parse_dates=date_cols_1,
                    dtype={
                        "ORDEM_EXERC": "category",
                        "CD_CVM": "category",
                        "CD_CONTA": "category",
                        "ESCALA_MOEDA": "category",
                        "MOEDA": "category",
                        "DS_CONTA": "category",
                        "ST_CONTA_FIXA": "category",
                    },
                )
            except ValueError:
                try:
                    dfp = pd.read_csv(
                        arq_zip.open(planilha),
                        sep=";",
                        encoding="iso-8859-1",
                        parse_dates=date_cols_2,
                        dtype={
                            "ORDEM_EXERC": "category",
                            "CD_CVM": "category",
                            "CD_CONTA": "category",
                            "ESCALA_MOEDA": "category",
                            "MOEDA": "category",
                            "DS_CONTA": "category",
                            "ST_CONTA_FIXA": "category",
                        },
                    )

                except ValueError:
                    try:
                        dfp = pd.read_csv(
                            arq_zip.open(planilha),
                            sep=";",
                            encoding="iso-8859-1",
                            parse_dates=["DT_REFER"],
                            dtype={"ORDEM_EXERC": "category", "CD_CVM": "category"},
                        )
                    except Exception as exc:
                        print("erro:", planilha, " | ", exc)

            list_demonstracoes.append(dfp)
            # cols.append(dfp.columns)
            # print(dfp.dtypes)
            # print(dfp.memory_usage())

    base_cvm = pd.concat(list_demonstracoes)

    base_cvm[["con_ind", "tipo_dem"]] = base_cvm["GRUPO_DFP"].str.split(
        "-", expand=True
    )
    base_cvm["con_ind"] = base_cvm["con_ind"].str.strip()
    base_cvm["tipo_dem"] = base_cvm["tipo_dem"].str.strip()

    base_cvm = base_cvm[base_cvm["ORDEM_EXERC"] != "PENÚLTIMO"]

    base_cvm.to_parquet(path=f"{CWD}\\dados_concat.parquet")


# %%

data = pd.read_parquet("dados_concat.parquet")

ativos = data.filter(items=["CNPJ_CIA", "DENOM_CIA", "CD_CVM"])
ativos.drop_duplicates(["CD_CVM"], inplace=True, ignore_index=True)

ativos_dict = ativos.to_dict(orient="index")

# %%
from interface.Interface import CollectionAtivos
from core.AtivosCore import Ativos

repo = CollectionAtivos()

# %%
itub = data[data["DENOM_CIA"] == "ITAU UNIBANCO HOLDING S.A."]
itub = itub[itub["DT_FIM_EXERC"] >= "2022-01-01"]
itub = itub[itub["DT_FIM_EXERC"] <= "2022-12-31"]

# %%


# %%
