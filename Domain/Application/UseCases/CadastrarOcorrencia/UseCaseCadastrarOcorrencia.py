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



        insertOcorrencia = f'INSERT INTO occurrences (gbif_id, event_date, locality) VALUES ({gbif_id},"{event_date}","{locality}");'
        insertTaxonomia = f'INSERT INTO taxonomy (fk_kingdom_key, fk_phylum_key, fk_class_key, fk_order_key, fk_family_key, fk_genus_key, accepted_scientific_name, fk_gbif_id) VALUES ((SELECT kingdom_key FROM kingdoms WHERE "{kingdom}" = kingdom_name), (SELECT phylum_key FROM phylums WHERE "{phylum}" = phylum_name), (SELECT class_key FROM classes WHERE "{classe}" = class_name), (SELECT order_key FROM orders WHERE "{order}" = order_name), (SELECT family_key FROM families WHERE "{family}" = family_name), (SELECT genus_key FROM genus WHERE "{genus}" = genus_name), accepted_scientific_name, fk_gbif_id);'
        cursor.execute(insertOcorrencia)
        cursor.execute(insertTaxonomia)
        connection.commit()
        connection.close()
        __BaseReturn.SuccessDataBase()
        return __BaseReturn.SuccessCadastro()

    except:
        __BaseReturn.ErrorDataBase()