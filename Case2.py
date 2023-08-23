from teste_request import requisicao
import Textos.postagens as j

requisicao = requisicao('https://jsonplaceholder.typicode.com/users')

postagem = j.postagem()

postagem_alterada = j.postagem_alterada()

requisicao.validar_get()
requisicao.validar_post(postagem)
requisicao.validar_put(postagem_alterada)
requisicao.validar_delete()
requisicao.validar_json()
