from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *

#admin.site.register(Table, SimpleHistoryAdmin)
class TableHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['id', 'col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7', 'col_8'
    , 'col_9', 'col_10', 'col_11', 'col_12', 'col_13', 'col_14', 'col_15', 'col_16', 'col_17', 'col_18', 'col_19', 'col_20',
    'col_21', 'col_22', 'col_23']
    list_editable  = ['col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7', 'col_8'
    , 'col_9', 'col_10', 'col_11', 'col_12', 'col_13', 'col_14', 'col_15', 'col_16', 'col_17', 'col_18', 'col_19', 'col_20',
    'col_21', 'col_22', 'col_23']

admin.site.register(Table, TableHistoryAdmin)

class DocumentHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['id', 'description', 'document', 'uploaded_at', 'status']

admin.site.register(Document, DocumentHistoryAdmin)
