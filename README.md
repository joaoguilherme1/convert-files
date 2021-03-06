<h1 align="center">
  Helpmydoc - README versão PT-BR
</h1>
<h1 align="center">
  <a href="http://helpmydoc.net/">helpmydoc.net</a>
</h1>

<p align="center">
  <img alt="GitHub" src="https://img.shields.io/github/license/joaoguilherme1/convert-files?style=for-the-badge">
<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/joaoguilherme1/convert-files?style=for-the-badge">
<img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/joaoguilherme1/convert-files?color=green&style=for-the-badge">
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/joaoguilherme1/convert-files?style=for-the-badge">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/joaoguilherme1/convert-files?style=for-the-badge">
<img alt="Website" src="https://img.shields.io/website?style=for-the-badge&url=http%3A%2F%2Fhelpmydoc.net%2F">
</p>

### Sumário

1. [Descrição/Resumo](#descrição)
2. [Pré-requisitos](#pre-requisitos)
3. [Rodando o projeto/Instalação](#instalação)
4. [Conhecimento adquirido no projeto](#conhecimento)
5. [Licença](#licença)

<hr>

## 1. Descrição / Resumo <a name="descrição"></a>

O website tem como uma de suas funções explorar a pasta /tmp/ que estão disponiveis na maioria da distros linux, de maneira que, ao usuario enviar um arquivo, o servidor consiga baixar e em seguida ja converter o arquivo guardando-o no sistema por um periodo curto de tempo até que ele seja deletado.

Foi pensado também na simplicidade com que o usuario poderia enviar os arquivos, e principalmente tornando o site open-source para que todos possam colaborar.

A pasta /tmp/ é configurada na máquina de modo que de 30 em 30 minutos o sistema reboota e os arquivos presentes nela são deletados, portanto isso é a garantia ded que os arquivos não ficam salvos.

## 2. Pré-requisitos <a name="pre-requisitos"></a>


## 3. Instalação

```
#Ambiente linux

#instalando vitualenv
$ python3 -m venv <nome_da_venv_aqui>

#clonando o repositorio
$ git clone https://github.com/joaoguilherme1/convert-files

#instalando os arquivos do projeto
pip install -r /caminho/para/requirements.txt
```

<p>Para subir o repositório no github foi necessario esconder algumas chaves do projeto. então sera necessario criar um arquivo chamado credenciais.py no caminho /tudoparapdf/tudoparapdf/credenciais.py com o conteudo :</p>

```
#conteudo do arquivo

chave = SUA_CHAVE_DJANGO
hosts = []
status = True
```

## 4. Conhecimento adquirido no projeto <a name="conhecimento"></a>

Ferramentas usadas nesse projeto:

- Python
	- Django
- Javascript
- HTML
- CSS
	- Bootstrap
- AWS
	- EC2
		- Ubuntu
	- Route 53
	- CloudWatch
- uWSGI
- Nginx


## 5. Licença <a name="licença"></a>

MIT License - Veja o arquivo [LICENSE.md](LICENSE.md)
