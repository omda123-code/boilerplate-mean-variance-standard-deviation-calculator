{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM4fMFEPuHcLfJ7Kfjug6XZ",
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
        "<a href=\"https://colab.research.google.com/github/omda123-code/boilerplate-mean-variance-standard-deviation-calculator/blob/main/mean_var_std.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "s4vVel3mElAQ"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "\n",
        "def calculate(input_list):\n",
        "    if len(input_list) != 9:\n",
        "        raise ValueError(\"List must contain nine numbers.\")\n",
        "\n",
        "    matrix = np.array(input_list).reshape(3, 3)\n",
        "\n",
        "    calculations = {\n",
        "        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().item()],\n",
        "        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().item()],\n",
        "        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().item()],\n",
        "        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().item()],\n",
        "        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().item()],\n",
        "        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().item()]\n",
        "    }\n",
        "\n",
        "    return calculations\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "IPgounB7E3OA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "FvRDB41tE3_M"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}