from Adapters.NeonPostgress import NeonPostgressService
from Domain.Core.Base import BaseReturn

__Neon = NeonPostgressService
__BaseReturn = BaseReturn

def enviarDadosFormulario():
    try:
        __DatabaseStringConnect = "postgresql://aranducontact:AHBk4X0TLtNb@ep-billowing-disk-92753043.us-east-2.aws.neon.tech/ProjetoBanco?sslmode=require"

        connection, cursor = __Neon.GetConnection(__DatabaseStringConnect)
        Reinos = list(__Neon.GetView(cursor, "kingdom_names"))
        Filos = list(__Neon.GetView(cursor, "phylum_names"))
        Classes = list(__Neon.GetView(cursor, "class_names"))
        Ordens = list(__Neon.GetView(cursor, "order_names"))
        Familias = list(__Neon.GetView(cursor, "family_names"))
        Generos = list(__Neon.GetView(cursor, "genus_names"))
        Especies = list(__Neon.GetView(cursor, "species_names"))
        connection.close()
        __BaseReturn.SuccessDataBase()
        return Reinos, Filos, Classes, Ordens, Familias, Generos, Especies
    except:
        __BaseReturn.ErrorDataBase()