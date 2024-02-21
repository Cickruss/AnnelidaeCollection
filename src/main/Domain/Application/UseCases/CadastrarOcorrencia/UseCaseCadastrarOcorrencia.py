from Adapters.NeonPostgress import NeonPostgressService
from Domain.Core.Base import BaseReturn

__Neon = NeonPostgressService
__BaseReturn = BaseReturn


def CadastrarOcorrencia(ocorrencia):
    try:
        __DatabaseStringConnect = "postgresql://aranducontact:AHBk4X0TLtNb@ep-billowing-disk-92753043.us-east-2.aws.neon.tech/ProjetoBanco?sslmode=require"
        connection, cursor = __Neon.GetConnection(__DatabaseStringConnect)

        gbifId = ocorrencia.GBIF
        data = str(ocorrencia.data)
        nomeCientifico = str(ocorrencia.nome_cientifico)
        localidade = f'{ocorrencia.estado},{ocorrencia.cidade}'
        reino = str(ocorrencia.reino).replace('(','').replace(')','').replace(',','').replace("'",'')
        filo = str(ocorrencia.filo).replace('(','').replace(')','').replace(',','').replace("'",'')
        classe = str(ocorrencia.classe).replace('(','').replace(')','').replace(',','').replace("'",'')
        ordem = str(ocorrencia.ordem).replace('(','').replace(')','').replace(',','').replace("'",'')
        familia = str(ocorrencia.familia).replace('(','').replace(')','').replace(',','').replace("'",'')
        genero = str(ocorrencia.genero).replace('(','').replace(')','').replace(',','').replace("'",'')


        insertTaxonomia = f"INSERT INTO taxonomy (fk_kingdom_key, fk_phylum_key, fk_class_key, fk_order_key, fk_family_key, fk_genus_key, accepted_scientific_name, fk_gbif_id) VALUES ((SELECT kingdom_key FROM kingdoms WHERE name = '{reino}'), (SELECT phylum_key FROM phylums WHERE '{filo}' = name), (SELECT class_key FROM classes WHERE '{classe}' = name), (SELECT order_key FROM orders WHERE '{ordem}' = name), (SELECT family_key FROM families WHERE '{familia}' = name), (SELECT genus_key FROM genus WHERE '{genero}' = name), '{nomeCientifico}', {gbifId});"
        insertOcorrencia = f"INSERT INTO occurrences (gbif_id, event_date, higher_geography) VALUES ({gbifId},'{data}','{localidade}');"
        cursor.execute(insertOcorrencia)
        connection.commit()
        cursor.execute(insertTaxonomia)
        connection.commit()
        connection.close()
        return __BaseReturn.SuccessCadastro()
    except:
        __BaseReturn.ErrorDataBase()