from Adapters.NeonPostgress import NeonPostgressService
from Domain.Core.Base import BaseReturn

__Neon = NeonPostgressService
__BaseReturn = BaseReturn


def EnviarDadosGraficos():
    try:
        __DatabaseStringConnect = "postgresql://aranducontact:AHBk4X0TLtNb@ep-billowing-disk-92753043.us-east-2.aws.neon.tech/ProjetoBanco?sslmode=require"

        connection, cursor = __Neon.GetConnection(__DatabaseStringConnect)
        TotalOcorrencias = __Neon.GetView(cursor, "total_occurrences_view")
        CidadesMaiores = __Neon.GetView(cursor, "top_cities_occurrences")
        EspeciesMaiores = __Neon.GetView(cursor, "species_count_view")

        connection.close()
        __BaseReturn.SuccessDataBase()
        return CidadesMaiores, EspeciesMaiores
    except:
        __BaseReturn.ErrorDataBase()
