from Adapters.NeonPostgress import NeonPostgressService
from Domain.Core.Base import BaseReturn

__Neon = NeonPostgressService
__BaseReturn = BaseReturn


def EnviarDadosGraficos():
    try:
        __DatabaseStringConnect = "postgresql://aranducontact:AHBk4X0TLtNb@ep-billowing-disk-92753043.us-east-2.aws.neon.tech/ProjetoBanco?sslmode=require"

        connection, cursor = __Neon.GetConnection(__DatabaseStringConnect)
        kingdoms_occurrences = __Neon.GetView(cursor, "occurrences_by_kingdom_view")
        phylums_occurrences = __Neon.GetView(cursor, "occurrences_by_phylum_view")
        classes_occurrences = __Neon.GetView(cursor, "occurrences_by_class_view")
        orders_occurrences = __Neon.GetView(cursor, "occurrences_by_order_view")
        families_occurrences = __Neon.GetView(cursor, "occurrences_by_family_view")
        genus_occurrences = __Neon.GetView(cursor, "occurrences_by_genus_view")
        species_occurrences = __Neon.GetView(cursor, "occurrences_by_species_view")

        connection.close()
        __BaseReturn.SuccessDataBase()
        return {
            "kingdoms": kingdoms_occurrences,
            "phylums": phylums_occurrences,
            "classes": classes_occurrences,
            "kingdoms": orders_occurrences,
            "families": families_occurrences,
            "genus": genus_occurrences,
            "species": species_occurrences
        }

    except:
        __BaseReturn.ErrorDataBase()
