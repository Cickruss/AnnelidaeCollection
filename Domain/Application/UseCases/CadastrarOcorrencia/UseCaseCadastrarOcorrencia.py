from Adapters.NeonPostgress import NeonPostgressService
from Domain.Core.Base import BaseReturn

__Neon = NeonPostgressService
__BaseReturn = BaseReturn


def CadastrarOcorrencia(ocorrencia):
    try:
        __DatabaseStringConnect = "postgresql://aranducontact:AHBk4X0TLtNb@ep-billowing-disk-92753043.us-east-2.aws.neon.tech/ProjetoBanco?sslmode=require"
        connection, cursor = __Neon.GetConnection(__DatabaseStringConnect)

        gbif_id = ocorrencia.GBIF
        event_date = ocorrencia.data
        locality = f'{ocorrencia.estado},{ocorrencia.cidade}'
        kingdom = ocorrencia.reino
        phylum = ocorrencia.filo
        classe = ocorrencia.classe
        order = ocorrencia.order
        family = ocorrencia.familia
        genus = family.genero



        insertOcorrencia = f'INSERT  INTO  () VALUES ()'
        cursor.execute(insertOcorrencia)
        connection.commit()
        connection.close()
        __BaseReturn.SuccessDataBase()
        return __BaseReturn.SuccessCadastro()

    except:
        __BaseReturn.ErrorDataBase()