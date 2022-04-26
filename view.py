import controller
from models.LinkedList import LinkedList
def sistema_paises():
    lista_ligada = LinkedList()
    while True:
        try:

            input_user = input().split(" ")
        except EOFError:
            return

        if input_user[0] == "RPI":
            if controller.inserir_inicio_lista(lista_ligada, input_user[1]):
                lista_ligada.traverse_list()

        if input_user[0] == "RPF":
            if controller.inserir_fim_lista(lista_ligada, input_user[1]):
                lista_ligada.traverse_list()

        if input_user[0] == "RPDE":
            if controller.registar_depois_elemento(lista_ligada, input_user[1], input_user[2]):
                lista_ligada.traverse_list()
            
        if input_user[0] == "RPAE":
            if controller.registar_antes_elemento(lista_ligada, input_user[1], input_user[2]):
                lista_ligada.traverse_list()

            
        if input_user[0] == "RPII":
            if controller.registar_pais_indice(lista_ligada, input_user[2], input_user[1]):
                lista_ligada.traverse_list()

        if input_user[0] == "VNE":
            if controller.verificar_numero_paises(lista_ligada):
                print(f"O número de elementos é {lista_ligada.get_count()}.")

            
        if input_user[0] == "VP":
            if controller.verificar_pais(lista_ligada, input_user[1]):
                print(f"O país {input_user[1]} encontra-se na lista.")
            else:
                print(f"O país {input_user[1]} não se encontra na lista.")
            
        if input_user[0] == "EPE":
            primeiro_pais = lista_ligada.start_node.item
            if controller.eliminar_primeiro_pais(lista_ligada):
                print(f"O país {primeiro_pais} foi eliminado da lista.")
            
        if input_user[0] == "EUE":
            ultimo_pais = lista_ligada.get_last_node()
            if controller.eliminar_ultimo_pais(lista_ligada):
                print(f"O país {ultimo_pais} foi eliminado da lista.")
            
        if input_user[0] == "EP":
            if controller.verificar_pais(lista_ligada, input_user[1]):
                controller.eliminar_pais(lista_ligada, input_user[1])
                
                print(f"O país {input_user[1]} foi eliminado da lista.")
            else:
                print(f"O país {input_user[1]} não se encontra na lista.")
            