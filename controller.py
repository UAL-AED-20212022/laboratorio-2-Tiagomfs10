from models.LinkedList import LinkedList
def inserir_inicio_lista(lista_ligada, elemento):
    lista_ligada.insert_at_start(elemento)
    return lista_ligada

def inserir_fim_lista(lista_ligada, elemento):
    lista_ligada.insert_at_end(elemento)
    return lista_ligada

def registar_depois_elemento(lista_ligada, elemento1, registado):
    lista_ligada.insert_after_item(elemento1, registado)
    return lista_ligada

def registar_antes_elemento(lista_ligada, elemento1, registado):
    lista_ligada.insert_before_item(elemento1, registado)
    return lista_ligada

def registar_pais_indice(lista_ligada, elemento2, elemento1):
    lista_ligada.insert_at_index(int(elemento2), elemento1)
    return lista_ligada

def verificar_numero_paises(lista_ligada):
    lista_ligada.get_count()
    return lista_ligada

def verificar_pais(lista_ligada, elemento):
    if lista_ligada.search_item(elemento) == True:
        return True, lista_ligada
    else:
        return False

def eliminar_primeiro_pais(lista_ligada):
    lista_ligada.delete_at_start()
    return lista_ligada

def eliminar_ultimo_pais(lista_ligada):
    lista_ligada.delete_at_end()
    return lista_ligada
    
def eliminar_pais(lista_ligada, elemento):
    lista_ligada.delete_element_by_value(elemento)
    return lista_ligada