{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rgm12345/enap_python3/blob/main/Encerramento_mod3_Reb.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Objetivo*: Praticar o uso de dashboards usando o Streamlit e o GitHub."
      ],
      "metadata": {
        "id": "fdKBpVbaAAwW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Questão 1"
      ],
      "metadata": {
        "id": "ECYxYU86AGuT"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Tema: A distribuição de gênero na Câmara dos Deputados**\n",
        "\n",
        "O Ministério da Fazenda, em sua iniciativa de promover a inclusão feminina, solicitou um estudo para entender melhor a representatividade de gênero na Câmara dos Deputados. O objetivo inicial é coletar e divulgar dados sobre a distribuição de deputados (homens e mulheres) por estado. Com esses dados, você deverá desenvolver um dashboard público que apresente essas informações de forma acessível à população.\n",
        "O dashboard deverá ser atualizado automaticamente a cada eleição, refletindo as mudanças na composição de gênero da Câmara dos Deputados.\n",
        "\n",
        "\n",
        "Usando a API da câmara dos deputados disponível no link https://dadosabertos.camara.leg.br/swagger/api.html, selecione um dos URL endpoints pra criar um dashboard no streamlit que mostre o gráfico de barras no número de homens e mulheres deputados por estado. Além disso, o programa deve mostrar o total de deputados, além da porcentagem de homens e mulheres.\n",
        "\n",
        "Dicas: Procure uma API que retorne os dados dos deputados por sexo. A seguir, recupere os dados dos deputados e deputadas e insira em dois dataframes diferentes. Na sequência, use o comando concat para unir os dois dataframes.\n",
        "\n",
        "*Sugestões (e não obrigação) de passos a serem seguidos:*\n",
        "1. Instale o streamlit;\n",
        "2. Importe os módulos requests, pandas e streamlit.\n",
        "3. A partir dos dados abertos da camara dos deputados (https://dadosabertos.camara.leg.br/swagger/api.html) defina a URL da API com informações sobre os deputados, incluindo a informação sobre o gênero. DICA: Use a opção de deputados.\n",
        "4. Faça a importação dos dados de deputadas mulheres (dfmulheres) e dos deputados homens (dfhomens) e faça a concatenação dos dataframes usando o comando concat.\n",
        "5. Crie um dashboard no streamlit com essas informações e insira um selectbox que realize filtragem por gênero.\n",
        "6. Crie um gráfico de barras com o número de homens e mulheres deputados por estado, a depender do sexo selecionado. Se necessário, peça ajuda ao chat GPT sobre como calcular a quantidade de deputados por estado.\n",
        "7. Acrescente informações sobre o total de deputados, além do total de homens e mulheres."
      ],
      "metadata": {
        "id": "qSbggQ5qAI6j"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "d8RDtsUy_3Nd",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "outputId": "2a56e197-f96c-4a86-fbe1-7605d59d5960"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.40.1-py2.py3-none-any.whl.metadata (8.5 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<3,>=1.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (11.0.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.25.5)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (17.0.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.9.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.1.43)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2024.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.4.0)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.8.30)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.21.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.16.0)\n",
            "Downloading streamlit-1.40.1-py2.py3-none-any.whl (8.6 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.6/8.6 MB\u001b[0m \u001b[31m26.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m55.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m5.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.40.1 watchdog-6.0.0\n"
          ]
        }
      ],
      "source": [
        "pip install streamlit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import streamlit as st\n",
        "import requests as req"
      ],
      "metadata": {
        "id": "KuQPIDTVP9tv"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "url_F = \"https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome\"\n",
        "url_M = \"https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome\"\n",
        "\n",
        "api_F = req.get(url_F)\n",
        "api_F = api_F.json()\n",
        "\n",
        "api_M = req.get(url_M)\n",
        "api_M = api_M.json()"
      ],
      "metadata": {
        "id": "HCxqWaMkQWzU"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "api_F['dados'][0]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "M_unfMpRQh9t",
        "outputId": "9ee9b4a9-e683-4951-863e-b1f6cd1943d6"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'id': 204528,\n",
              " 'uri': 'https://dadosabertos.camara.leg.br/api/v2/deputados/204528',\n",
              " 'nome': 'Adriana Ventura',\n",
              " 'siglaPartido': 'NOVO',\n",
              " 'uriPartido': 'https://dadosabertos.camara.leg.br/api/v2/partidos/37901',\n",
              " 'siglaUf': 'SP',\n",
              " 'idLegislatura': 57,\n",
              " 'urlFoto': 'https://www.camara.leg.br/internet/deputado/bandep/204528.jpg',\n",
              " 'email': 'dep.adrianaventura@camara.leg.br'}"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "api_M[\"dados\"][0]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mV4dnNyyT4YO",
        "outputId": "4a89122a-c7d4-4d42-e21c-b7cc55bdd029"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'id': 220593,\n",
              " 'uri': 'https://dadosabertos.camara.leg.br/api/v2/deputados/220593',\n",
              " 'nome': 'Abilio Brunini',\n",
              " 'siglaPartido': 'PL',\n",
              " 'uriPartido': 'https://dadosabertos.camara.leg.br/api/v2/partidos/37906',\n",
              " 'siglaUf': 'MT',\n",
              " 'idLegislatura': 57,\n",
              " 'urlFoto': 'https://www.camara.leg.br/internet/deputado/bandep/220593.jpg',\n",
              " 'email': 'dep.abiliobrunini@camara.leg.br'}"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_dep_F = pd.DataFrame(api_F['dados'])\n",
        "df_dep_F[\"genero\"] = \"F\"\n",
        "\n",
        "df_dep_M = pd.DataFrame(api_M['dados'])\n",
        "df_dep_M[\"genero\"] = \"M\""
      ],
      "metadata": {
        "id": "0G2p-vA6Stum"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_dep = pd.concat([df_dep_F, df_dep_M])"
      ],
      "metadata": {
        "id": "xM1E5ZMLUCBD"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_dep.sample(2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 184
        },
        "id": "3PLggw4KS23i",
        "outputId": "33feb947-9425-47f1-edb7-6fe1da8cad6f"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         id                                                uri  \\\n",
              "227  204497  https://dadosabertos.camara.leg.br/api/v2/depu...   \n",
              "33   220674  https://dadosabertos.camara.leg.br/api/v2/depu...   \n",
              "\n",
              "                      nome siglaPartido  \\\n",
              "227         Júnior Ferrari          PSD   \n",
              "33   Dra. Alessandra Haber          MDB   \n",
              "\n",
              "                                            uriPartido siglaUf  idLegislatura  \\\n",
              "227  https://dadosabertos.camara.leg.br/api/v2/part...      PA             57   \n",
              "33   https://dadosabertos.camara.leg.br/api/v2/part...      PA             57   \n",
              "\n",
              "                                               urlFoto  \\\n",
              "227  https://www.camara.leg.br/internet/deputado/ba...   \n",
              "33   https://www.camara.leg.br/internet/deputado/ba...   \n",
              "\n",
              "                                     email genero  \n",
              "227        dep.juniorferrari@camara.leg.br      M  \n",
              "33   dep.dra.alessandrahaber@camara.leg.br      F  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-8e923dbe-3960-4364-b286-7b11427c4537\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id</th>\n",
              "      <th>uri</th>\n",
              "      <th>nome</th>\n",
              "      <th>siglaPartido</th>\n",
              "      <th>uriPartido</th>\n",
              "      <th>siglaUf</th>\n",
              "      <th>idLegislatura</th>\n",
              "      <th>urlFoto</th>\n",
              "      <th>email</th>\n",
              "      <th>genero</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>227</th>\n",
              "      <td>204497</td>\n",
              "      <td>https://dadosabertos.camara.leg.br/api/v2/depu...</td>\n",
              "      <td>Júnior Ferrari</td>\n",
              "      <td>PSD</td>\n",
              "      <td>https://dadosabertos.camara.leg.br/api/v2/part...</td>\n",
              "      <td>PA</td>\n",
              "      <td>57</td>\n",
              "      <td>https://www.camara.leg.br/internet/deputado/ba...</td>\n",
              "      <td>dep.juniorferrari@camara.leg.br</td>\n",
              "      <td>M</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>33</th>\n",
              "      <td>220674</td>\n",
              "      <td>https://dadosabertos.camara.leg.br/api/v2/depu...</td>\n",
              "      <td>Dra. Alessandra Haber</td>\n",
              "      <td>MDB</td>\n",
              "      <td>https://dadosabertos.camara.leg.br/api/v2/part...</td>\n",
              "      <td>PA</td>\n",
              "      <td>57</td>\n",
              "      <td>https://www.camara.leg.br/internet/deputado/ba...</td>\n",
              "      <td>dep.dra.alessandrahaber@camara.leg.br</td>\n",
              "      <td>F</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-8e923dbe-3960-4364-b286-7b11427c4537')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-8e923dbe-3960-4364-b286-7b11427c4537 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-8e923dbe-3960-4364-b286-7b11427c4537');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-3288d54c-48e3-442b-a655-e564e75bd3cf\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-3288d54c-48e3-442b-a655-e564e75bd3cf')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-3288d54c-48e3-442b-a655-e564e75bd3cf button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"df_dep\",\n  \"rows\": 2,\n  \"fields\": [\n    {\n      \"column\": \"id\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 11438,\n        \"min\": 204497,\n        \"max\": 220674,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          220674,\n          204497\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"uri\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"https://dadosabertos.camara.leg.br/api/v2/deputados/220674\",\n          \"https://dadosabertos.camara.leg.br/api/v2/deputados/204497\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"nome\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Dra. Alessandra Haber\",\n          \"J\\u00fanior Ferrari\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"siglaPartido\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"MDB\",\n          \"PSD\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"uriPartido\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"https://dadosabertos.camara.leg.br/api/v2/partidos/36899\",\n          \"https://dadosabertos.camara.leg.br/api/v2/partidos/36834\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"siglaUf\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 1,\n        \"samples\": [\n          \"PA\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"idLegislatura\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 57,\n        \"max\": 57,\n        \"num_unique_values\": 1,\n        \"samples\": [\n          57\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"urlFoto\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"https://www.camara.leg.br/internet/deputado/bandep/220674.jpg\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"email\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"dep.dra.alessandrahaber@camara.leg.br\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"genero\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"F\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "st.title(\"Distribuição de gênero na Câmara dos Deputados\")\n",
        "\n",
        "#total de homens\n",
        "st.metric('Total de Homens', df_dep_M['id'].count())\n",
        "#total de mulheres\n",
        "st.metric('Total de Mulheres', df_dep_F['id'].count())\n",
        "\n",
        "#item 5\n",
        "#Filtrando df por sexo\n",
        "#inserindo um selectbox\n",
        "filtro_gen = st.selectbox(\n",
        "    'Qual o gênero cuja distribuição por UF que deseja visualizar?',\n",
        "     df_dep['genero'].unique())\n",
        "\n",
        "df_filtrado = df_dep[df_dep['genero'] == filtro_gen]\n",
        "st.title('Distribuição por UF de Deputados do gênero ' + filtro_gen)\n",
        "\n",
        "\n",
        "st.bar_chart(df_filtrado,\n",
        "             x = 'siglaUf',\n",
        "             y = 'id',\n",
        "             x_label='Siglas dos estados',\n",
        "             y_label='Quantidade de deputados')\n",
        "\n",
        "\n",
        "\n",
        "st.write('A distribuição de gênero para a Câmara dos Deputados é a seguinte:')\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6eczuEzwa_Q1",
        "outputId": "0f7fc8ed-bd66-4ffb-a96a-a96b84bf92e1"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-11-18 14:04:34.366 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:34.369 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:34.373 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:34.375 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:34.377 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:34.379 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:34.382 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:34.385 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:34.390 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:34.396 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:34.397 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:34.400 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:34.405 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:34.407 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:34.758 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:35.540 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:35.547 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:35.548 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:35.550 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-18 14:04:35.552 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Questão 2 (para fazer em casa!)"
      ],
      "metadata": {
        "id": "wDqxqgo-ALbL"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ainda usando a API da câmara dos deputados, procure por um id de um deputado da questão anterior, por exemplo 74646 que corresponde ao deputado Aécio Neves, e calcule as despesas do deputado. A seguir, use o comando metrics para inserir esta despesa em seu dashboard. Dica: Procure por uma API que tenha dados de despesas dos deputados.\n",
        "\n",
        "*Sugestões (e não obrigação) de passos a serem seguidos:*\n",
        "1. Importe os módulos requests, pandas e streamlit.\n",
        "2. Copie o link da API usado na questão anterior e cole no navegador de sua preferência. A seguir, examine os dados mostrados e busque pelo ID de um deputado de sua preferência.\n",
        "3. Carregue os dados em um dataframe.\n",
        "4. Faça o cálculos dos dados usando uma das colunas disponíveis na busca.\n",
        "5. Usando a a função metrics do módulo Streamlit, informe os gastos do deputado escolhido."
      ],
      "metadata": {
        "id": "8ef-lNA3ANEL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "st"
      ],
      "metadata": {
        "id": "31jArc1SATvr"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}