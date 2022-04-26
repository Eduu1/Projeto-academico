{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "07264c2e-8ec7-4dd5-9668-31263aef8b4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# importando as bibliotecas\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "066cb229-182e-40db-b550-d2ddd08f844d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>symboling</th>\n",
       "      <th>normalized-losses</th>\n",
       "      <th>make</th>\n",
       "      <th>fuel-type</th>\n",
       "      <th>aspiration</th>\n",
       "      <th>num-of-doors</th>\n",
       "      <th>body-style</th>\n",
       "      <th>drive-wheels</th>\n",
       "      <th>engine-location</th>\n",
       "      <th>wheel-base</th>\n",
       "      <th>...</th>\n",
       "      <th>engine-size</th>\n",
       "      <th>fuel-system</th>\n",
       "      <th>bore</th>\n",
       "      <th>stroke</th>\n",
       "      <th>compression-ratio</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>peak-rpm</th>\n",
       "      <th>city-mpg</th>\n",
       "      <th>highway-mpg</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>?</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>13495</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3</td>\n",
       "      <td>?</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>16500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>?</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>hatchback</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>94.5</td>\n",
       "      <td>...</td>\n",
       "      <td>152</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>2.68</td>\n",
       "      <td>3.47</td>\n",
       "      <td>9.0</td>\n",
       "      <td>154</td>\n",
       "      <td>5000</td>\n",
       "      <td>19</td>\n",
       "      <td>26</td>\n",
       "      <td>16500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>164</td>\n",
       "      <td>audi</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>fwd</td>\n",
       "      <td>front</td>\n",
       "      <td>99.8</td>\n",
       "      <td>...</td>\n",
       "      <td>109</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.4</td>\n",
       "      <td>10.0</td>\n",
       "      <td>102</td>\n",
       "      <td>5500</td>\n",
       "      <td>24</td>\n",
       "      <td>30</td>\n",
       "      <td>13950</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>164</td>\n",
       "      <td>audi</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>4wd</td>\n",
       "      <td>front</td>\n",
       "      <td>99.4</td>\n",
       "      <td>...</td>\n",
       "      <td>136</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.4</td>\n",
       "      <td>8.0</td>\n",
       "      <td>115</td>\n",
       "      <td>5500</td>\n",
       "      <td>18</td>\n",
       "      <td>22</td>\n",
       "      <td>17450</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>200</th>\n",
       "      <td>-1</td>\n",
       "      <td>95</td>\n",
       "      <td>volvo</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>...</td>\n",
       "      <td>141</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.78</td>\n",
       "      <td>3.15</td>\n",
       "      <td>9.5</td>\n",
       "      <td>114</td>\n",
       "      <td>5400</td>\n",
       "      <td>23</td>\n",
       "      <td>28</td>\n",
       "      <td>16845</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>201</th>\n",
       "      <td>-1</td>\n",
       "      <td>95</td>\n",
       "      <td>volvo</td>\n",
       "      <td>gas</td>\n",
       "      <td>turbo</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>...</td>\n",
       "      <td>141</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.78</td>\n",
       "      <td>3.15</td>\n",
       "      <td>8.7</td>\n",
       "      <td>160</td>\n",
       "      <td>5300</td>\n",
       "      <td>19</td>\n",
       "      <td>25</td>\n",
       "      <td>19045</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>202</th>\n",
       "      <td>-1</td>\n",
       "      <td>95</td>\n",
       "      <td>volvo</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>...</td>\n",
       "      <td>173</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.58</td>\n",
       "      <td>2.87</td>\n",
       "      <td>8.8</td>\n",
       "      <td>134</td>\n",
       "      <td>5500</td>\n",
       "      <td>18</td>\n",
       "      <td>23</td>\n",
       "      <td>21485</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>203</th>\n",
       "      <td>-1</td>\n",
       "      <td>95</td>\n",
       "      <td>volvo</td>\n",
       "      <td>diesel</td>\n",
       "      <td>turbo</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>...</td>\n",
       "      <td>145</td>\n",
       "      <td>idi</td>\n",
       "      <td>3.01</td>\n",
       "      <td>3.4</td>\n",
       "      <td>23.0</td>\n",
       "      <td>106</td>\n",
       "      <td>4800</td>\n",
       "      <td>26</td>\n",
       "      <td>27</td>\n",
       "      <td>22470</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>204</th>\n",
       "      <td>-1</td>\n",
       "      <td>95</td>\n",
       "      <td>volvo</td>\n",
       "      <td>gas</td>\n",
       "      <td>turbo</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>...</td>\n",
       "      <td>141</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.78</td>\n",
       "      <td>3.15</td>\n",
       "      <td>9.5</td>\n",
       "      <td>114</td>\n",
       "      <td>5400</td>\n",
       "      <td>19</td>\n",
       "      <td>25</td>\n",
       "      <td>22625</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>205 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     symboling normalized-losses         make fuel-type aspiration  \\\n",
       "0            3                 ?  alfa-romero       gas        std   \n",
       "1            3                 ?  alfa-romero       gas        std   \n",
       "2            1                 ?  alfa-romero       gas        std   \n",
       "3            2               164         audi       gas        std   \n",
       "4            2               164         audi       gas        std   \n",
       "..         ...               ...          ...       ...        ...   \n",
       "200         -1                95        volvo       gas        std   \n",
       "201         -1                95        volvo       gas      turbo   \n",
       "202         -1                95        volvo       gas        std   \n",
       "203         -1                95        volvo    diesel      turbo   \n",
       "204         -1                95        volvo       gas      turbo   \n",
       "\n",
       "    num-of-doors   body-style drive-wheels engine-location  wheel-base  ...  \\\n",
       "0            two  convertible          rwd           front        88.6  ...   \n",
       "1            two  convertible          rwd           front        88.6  ...   \n",
       "2            two    hatchback          rwd           front        94.5  ...   \n",
       "3           four        sedan          fwd           front        99.8  ...   \n",
       "4           four        sedan          4wd           front        99.4  ...   \n",
       "..           ...          ...          ...             ...         ...  ...   \n",
       "200         four        sedan          rwd           front       109.1  ...   \n",
       "201         four        sedan          rwd           front       109.1  ...   \n",
       "202         four        sedan          rwd           front       109.1  ...   \n",
       "203         four        sedan          rwd           front       109.1  ...   \n",
       "204         four        sedan          rwd           front       109.1  ...   \n",
       "\n",
       "     engine-size  fuel-system  bore  stroke compression-ratio horsepower  \\\n",
       "0            130         mpfi  3.47    2.68               9.0        111   \n",
       "1            130         mpfi  3.47    2.68               9.0        111   \n",
       "2            152         mpfi  2.68    3.47               9.0        154   \n",
       "3            109         mpfi  3.19     3.4              10.0        102   \n",
       "4            136         mpfi  3.19     3.4               8.0        115   \n",
       "..           ...          ...   ...     ...               ...        ...   \n",
       "200          141         mpfi  3.78    3.15               9.5        114   \n",
       "201          141         mpfi  3.78    3.15               8.7        160   \n",
       "202          173         mpfi  3.58    2.87               8.8        134   \n",
       "203          145          idi  3.01     3.4              23.0        106   \n",
       "204          141         mpfi  3.78    3.15               9.5        114   \n",
       "\n",
       "     peak-rpm city-mpg highway-mpg  price  \n",
       "0        5000       21          27  13495  \n",
       "1        5000       21          27  16500  \n",
       "2        5000       19          26  16500  \n",
       "3        5500       24          30  13950  \n",
       "4        5500       18          22  17450  \n",
       "..        ...      ...         ...    ...  \n",
       "200      5400       23          28  16845  \n",
       "201      5300       19          25  19045  \n",
       "202      5500       18          23  21485  \n",
       "203      4800       26          27  22470  \n",
       "204      5400       19          25  22625  \n",
       "\n",
       "[205 rows x 26 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# carregando o arquivo csv e atribuindo-o a variavel df \n",
    "df = pd.read_csv('Automobile_data.csv')\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d5394409-52e5-4cca-9c0f-d2ca18468771",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A dimensão do dataframe é (205, 26)\n"
     ]
    }
   ],
   "source": [
    "print('A dimensão do dataframe é {}'.format(df.shape))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8ad5ebcb-60e5-459b-9449-572c3eca7580",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "symboling              int64\n",
       "normalized-losses     object\n",
       "make                  object\n",
       "fuel-type             object\n",
       "aspiration            object\n",
       "num-of-doors          object\n",
       "body-style            object\n",
       "drive-wheels          object\n",
       "engine-location       object\n",
       "wheel-base           float64\n",
       "length               float64\n",
       "width                float64\n",
       "height               float64\n",
       "curb-weight            int64\n",
       "engine-type           object\n",
       "num-of-cylinders      object\n",
       "engine-size            int64\n",
       "fuel-system           object\n",
       "bore                  object\n",
       "stroke                object\n",
       "compression-ratio    float64\n",
       "horsepower            object\n",
       "peak-rpm              object\n",
       "city-mpg               int64\n",
       "highway-mpg            int64\n",
       "price                 object\n",
       "dtype: object"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# verificando o tipo das variaveis\n",
    "df.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "490f7494-000a-4d35-b69e-642fb668bb2a",
   "metadata": {},
   "source": [
    ">Vemos acima que existe algumas variáveis que estão classificadas com o tipo de dados incorreto.\n",
    "por exemplo a variável alvo 'price' está como uma variável **obeject** quando na verdade ela é uma \n",
    "variável do tipo **float**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4b3dd571-74e8-4606-9d03-9d6011fd50f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>symboling</th>\n",
       "      <th>wheel-base</th>\n",
       "      <th>length</th>\n",
       "      <th>width</th>\n",
       "      <th>height</th>\n",
       "      <th>curb-weight</th>\n",
       "      <th>engine-size</th>\n",
       "      <th>compression-ratio</th>\n",
       "      <th>city-mpg</th>\n",
       "      <th>highway-mpg</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.834146</td>\n",
       "      <td>98.756585</td>\n",
       "      <td>174.049268</td>\n",
       "      <td>65.907805</td>\n",
       "      <td>53.724878</td>\n",
       "      <td>2555.565854</td>\n",
       "      <td>126.907317</td>\n",
       "      <td>10.142537</td>\n",
       "      <td>25.219512</td>\n",
       "      <td>30.751220</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.245307</td>\n",
       "      <td>6.021776</td>\n",
       "      <td>12.337289</td>\n",
       "      <td>2.145204</td>\n",
       "      <td>2.443522</td>\n",
       "      <td>520.680204</td>\n",
       "      <td>41.642693</td>\n",
       "      <td>3.972040</td>\n",
       "      <td>6.542142</td>\n",
       "      <td>6.886443</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-2.000000</td>\n",
       "      <td>86.600000</td>\n",
       "      <td>141.100000</td>\n",
       "      <td>60.300000</td>\n",
       "      <td>47.800000</td>\n",
       "      <td>1488.000000</td>\n",
       "      <td>61.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>13.000000</td>\n",
       "      <td>16.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>94.500000</td>\n",
       "      <td>166.300000</td>\n",
       "      <td>64.100000</td>\n",
       "      <td>52.000000</td>\n",
       "      <td>2145.000000</td>\n",
       "      <td>97.000000</td>\n",
       "      <td>8.600000</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>25.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>97.000000</td>\n",
       "      <td>173.200000</td>\n",
       "      <td>65.500000</td>\n",
       "      <td>54.100000</td>\n",
       "      <td>2414.000000</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>30.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>2.000000</td>\n",
       "      <td>102.400000</td>\n",
       "      <td>183.100000</td>\n",
       "      <td>66.900000</td>\n",
       "      <td>55.500000</td>\n",
       "      <td>2935.000000</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>9.400000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>34.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>120.900000</td>\n",
       "      <td>208.100000</td>\n",
       "      <td>72.300000</td>\n",
       "      <td>59.800000</td>\n",
       "      <td>4066.000000</td>\n",
       "      <td>326.000000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>49.000000</td>\n",
       "      <td>54.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        symboling  wheel-base      length       width      height  \\\n",
       "count  205.000000  205.000000  205.000000  205.000000  205.000000   \n",
       "mean     0.834146   98.756585  174.049268   65.907805   53.724878   \n",
       "std      1.245307    6.021776   12.337289    2.145204    2.443522   \n",
       "min     -2.000000   86.600000  141.100000   60.300000   47.800000   \n",
       "25%      0.000000   94.500000  166.300000   64.100000   52.000000   \n",
       "50%      1.000000   97.000000  173.200000   65.500000   54.100000   \n",
       "75%      2.000000  102.400000  183.100000   66.900000   55.500000   \n",
       "max      3.000000  120.900000  208.100000   72.300000   59.800000   \n",
       "\n",
       "       curb-weight  engine-size  compression-ratio    city-mpg  highway-mpg  \n",
       "count   205.000000   205.000000         205.000000  205.000000   205.000000  \n",
       "mean   2555.565854   126.907317          10.142537   25.219512    30.751220  \n",
       "std     520.680204    41.642693           3.972040    6.542142     6.886443  \n",
       "min    1488.000000    61.000000           7.000000   13.000000    16.000000  \n",
       "25%    2145.000000    97.000000           8.600000   19.000000    25.000000  \n",
       "50%    2414.000000   120.000000           9.000000   24.000000    30.000000  \n",
       "75%    2935.000000   141.000000           9.400000   30.000000    34.000000  \n",
       "max    4066.000000   326.000000          23.000000   49.000000    54.000000  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# método para obter um resumo estatístico do dataframe. por padrão ele mostra os dados númericos\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9443f04e-ebe8-4579-a263-c0ce34b7c2f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>normalized-losses</th>\n",
       "      <th>make</th>\n",
       "      <th>fuel-type</th>\n",
       "      <th>aspiration</th>\n",
       "      <th>num-of-doors</th>\n",
       "      <th>body-style</th>\n",
       "      <th>drive-wheels</th>\n",
       "      <th>engine-location</th>\n",
       "      <th>engine-type</th>\n",
       "      <th>num-of-cylinders</th>\n",
       "      <th>fuel-system</th>\n",
       "      <th>bore</th>\n",
       "      <th>stroke</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>peak-rpm</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "      <td>205</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>52</td>\n",
       "      <td>22</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "      <td>39</td>\n",
       "      <td>37</td>\n",
       "      <td>60</td>\n",
       "      <td>24</td>\n",
       "      <td>187</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>?</td>\n",
       "      <td>toyota</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>fwd</td>\n",
       "      <td>front</td>\n",
       "      <td>ohc</td>\n",
       "      <td>four</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.62</td>\n",
       "      <td>3.4</td>\n",
       "      <td>68</td>\n",
       "      <td>5500</td>\n",
       "      <td>?</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>41</td>\n",
       "      <td>32</td>\n",
       "      <td>185</td>\n",
       "      <td>168</td>\n",
       "      <td>114</td>\n",
       "      <td>96</td>\n",
       "      <td>120</td>\n",
       "      <td>202</td>\n",
       "      <td>148</td>\n",
       "      <td>159</td>\n",
       "      <td>94</td>\n",
       "      <td>23</td>\n",
       "      <td>20</td>\n",
       "      <td>19</td>\n",
       "      <td>37</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       normalized-losses    make fuel-type aspiration num-of-doors body-style  \\\n",
       "count                205     205       205        205          205        205   \n",
       "unique                52      22         2          2            3          5   \n",
       "top                    ?  toyota       gas        std         four      sedan   \n",
       "freq                  41      32       185        168          114         96   \n",
       "\n",
       "       drive-wheels engine-location engine-type num-of-cylinders fuel-system  \\\n",
       "count           205             205         205              205         205   \n",
       "unique            3               2           7                7           8   \n",
       "top             fwd           front         ohc             four        mpfi   \n",
       "freq            120             202         148              159          94   \n",
       "\n",
       "        bore stroke horsepower peak-rpm price  \n",
       "count    205    205        205      205   205  \n",
       "unique    39     37         60       24   187  \n",
       "top     3.62    3.4         68     5500     ?  \n",
       "freq      23     20         19       37     4  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# utilizando o parametro include para filtra pelos dados do tipo object\n",
    "df.describe(include='object')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc4571b6-cfdf-4949-8037-1c445cd1008a",
   "metadata": {},
   "source": [
    "> Podemos observar claramente agora que as variáveis *'price'*, *'bore'* etc.. estão aparecendo no resumo estatístico \n",
    "para dados categóricos acima. \n",
    ">> Podemos notar também nessa breve exploração do conjunto de dados que temos alguns dados com o símbolo '?' \n",
    "e que teremos que tratá - los adiante"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2adddad2-b335-40bb-ad06-9b21143e1807",
   "metadata": {},
   "source": [
    "## Pré-Procecessamento dos dados"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "949a1cd7-2d47-4050-9647-9a15a9000e6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# utilizando o metodo replace para converter os símbolo '?' para NaN\n",
    "# fica melhor para tratarmos esses dados\n",
    "df1 = df.replace('?', np.NaN)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "dca90bbb-777c-4d40-a031-c0b948872d03",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>symboling</th>\n",
       "      <th>normalized-losses</th>\n",
       "      <th>make</th>\n",
       "      <th>fuel-type</th>\n",
       "      <th>aspiration</th>\n",
       "      <th>num-of-doors</th>\n",
       "      <th>body-style</th>\n",
       "      <th>drive-wheels</th>\n",
       "      <th>engine-location</th>\n",
       "      <th>wheel-base</th>\n",
       "      <th>...</th>\n",
       "      <th>engine-size</th>\n",
       "      <th>fuel-system</th>\n",
       "      <th>bore</th>\n",
       "      <th>stroke</th>\n",
       "      <th>compression-ratio</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>peak-rpm</th>\n",
       "      <th>city-mpg</th>\n",
       "      <th>highway-mpg</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>13495</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>16500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>hatchback</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>94.5</td>\n",
       "      <td>...</td>\n",
       "      <td>152</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>2.68</td>\n",
       "      <td>3.47</td>\n",
       "      <td>9.0</td>\n",
       "      <td>154</td>\n",
       "      <td>5000</td>\n",
       "      <td>19</td>\n",
       "      <td>26</td>\n",
       "      <td>16500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>164</td>\n",
       "      <td>audi</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>fwd</td>\n",
       "      <td>front</td>\n",
       "      <td>99.8</td>\n",
       "      <td>...</td>\n",
       "      <td>109</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.4</td>\n",
       "      <td>10.0</td>\n",
       "      <td>102</td>\n",
       "      <td>5500</td>\n",
       "      <td>24</td>\n",
       "      <td>30</td>\n",
       "      <td>13950</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>164</td>\n",
       "      <td>audi</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>4wd</td>\n",
       "      <td>front</td>\n",
       "      <td>99.4</td>\n",
       "      <td>...</td>\n",
       "      <td>136</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.4</td>\n",
       "      <td>8.0</td>\n",
       "      <td>115</td>\n",
       "      <td>5500</td>\n",
       "      <td>18</td>\n",
       "      <td>22</td>\n",
       "      <td>17450</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   symboling normalized-losses         make fuel-type aspiration num-of-doors  \\\n",
       "0          3               NaN  alfa-romero       gas        std          two   \n",
       "1          3               NaN  alfa-romero       gas        std          two   \n",
       "2          1               NaN  alfa-romero       gas        std          two   \n",
       "3          2               164         audi       gas        std         four   \n",
       "4          2               164         audi       gas        std         four   \n",
       "\n",
       "    body-style drive-wheels engine-location  wheel-base  ...  engine-size  \\\n",
       "0  convertible          rwd           front        88.6  ...          130   \n",
       "1  convertible          rwd           front        88.6  ...          130   \n",
       "2    hatchback          rwd           front        94.5  ...          152   \n",
       "3        sedan          fwd           front        99.8  ...          109   \n",
       "4        sedan          4wd           front        99.4  ...          136   \n",
       "\n",
       "   fuel-system  bore  stroke compression-ratio horsepower  peak-rpm city-mpg  \\\n",
       "0         mpfi  3.47    2.68               9.0        111      5000       21   \n",
       "1         mpfi  3.47    2.68               9.0        111      5000       21   \n",
       "2         mpfi  2.68    3.47               9.0        154      5000       19   \n",
       "3         mpfi  3.19     3.4              10.0        102      5500       24   \n",
       "4         mpfi  3.19     3.4               8.0        115      5500       18   \n",
       "\n",
       "  highway-mpg  price  \n",
       "0          27  13495  \n",
       "1          27  16500  \n",
       "2          26  16500  \n",
       "3          30  13950  \n",
       "4          22  17450  \n",
       "\n",
       "[5 rows x 26 columns]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# eliminando o os NaN da coluna 'price' passando o parametro axis=0 que seleciona as linhas\n",
    "df = df1.dropna(subset=['price'], axis=0)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "656db56d-31b9-4e7d-987b-4753b0378d2d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "symboling             0\n",
       "normalized-losses    37\n",
       "make                  0\n",
       "fuel-type             0\n",
       "aspiration            0\n",
       "num-of-doors          2\n",
       "body-style            0\n",
       "drive-wheels          0\n",
       "engine-location       0\n",
       "wheel-base            0\n",
       "length                0\n",
       "width                 0\n",
       "height                0\n",
       "curb-weight           0\n",
       "engine-type           0\n",
       "num-of-cylinders      0\n",
       "engine-size           0\n",
       "fuel-system           0\n",
       "bore                  4\n",
       "stroke                4\n",
       "compression-ratio     0\n",
       "horsepower            2\n",
       "peak-rpm              2\n",
       "city-mpg              0\n",
       "highway-mpg           0\n",
       "price                 0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# visualizando os valores faltantes no dataframe\n",
    "miss = df.isnull().sum()\n",
    "miss"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e221a7f-960f-4ac3-b16b-d1dd0f218c08",
   "metadata": {},
   "source": [
    "### Tratando valores missing"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "33a9a64a-7e1f-4559-86d8-a3d2f9e1b433",
   "metadata": {},
   "source": [
    "---\n",
    "Aqui farei a aplicação atribuindo a esses valores faltantes a média para cada coluna utilizando o método replace\n",
    "* Nessa parte estarei obtendo as médias para as colunas com valores NaN"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e49dc176-e114-473c-ae78-64e4868d9334",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Média de normalized-losses 122.0\n"
     ]
    }
   ],
   "source": [
    "# obtendo a média das colunas abaixo que tem os valores missing\n",
    "avg_norm = df['normalized-losses'].astype('float').mean(axis=0)\n",
    "print('Média de normalized-losses {}'.format(avg_norm))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a6fc8e7e-b328-4263-b763-b947a6f9b699",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Média para stroke 3.26\n"
     ]
    }
   ],
   "source": [
    "avg_stroke = df['stroke'].astype('float').mean(axis=0)\n",
    "print('Média para stroke {:.2f}'.format(avg_stroke))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "eb17b742-77b5-4402-a304-7aa53dd45d86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Média para bore 3.33\n"
     ]
    }
   ],
   "source": [
    "avg_bore = df['bore'].astype('float').mean(axis=0)\n",
    "print('Média para bore {:.2f}'.format(avg_bore))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b4a8f9a4-e537-4653-8c7d-2b03f2fdefa6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Média de horsepower 103.40\n"
     ]
    }
   ],
   "source": [
    "avg_horsepower = df['horsepower'].astype('float').mean(axis=0)\n",
    "print('Média de horsepower {:.2f}'.format(avg_horsepower))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4c85cdd4-de7f-4d83-a831-ff8ad7d5c3c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Média para peak-rpm 5117.59\n"
     ]
    }
   ],
   "source": [
    "avg_peak = df['peak-rpm'].astype('float').mean(axis=0)\n",
    "print('Média para peak-rpm {:.2f}'.format(avg_peak))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "617a7a6b-a073-4362-9e9b-4574c21351b2",
   "metadata": {},
   "source": [
    "* Nesta parte estarei utilizando o método replace para converter os valores NaN nas médias "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "24049e3e-1970-4d56-b14f-2f235df68c81",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['normalized-losses'].replace(np.NaN, avg_norm, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c0fcd21c-7d78-462a-bad7-aafee2053800",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['stroke'].replace(np.NaN, avg_stroke, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "1e19365a-b4b1-4634-a878-d2cedf36f122",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['bore'].replace(np.NaN, avg_bore, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3b74ff1c-a45e-4a73-acec-e7fb7b0a0df5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['horsepower'].replace(np.NaN, avg_horsepower, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "58f136c1-db44-497a-947f-1ba628233c71",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['peak-rpm'].replace(np.NaN, avg_peak, inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9fc2222c-e1ad-4af8-bfdb-99537714a75c",
   "metadata": {},
   "source": [
    "---\n",
    "Com essa variável *'num-of-doors'* como ela é categórica aplicarei o replace substituindo os NaN pela frequencia "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "7206f2ca-6ee4-4788-a2a0-9c8ef53a623a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "four    113\n",
       "two      86\n",
       "Name: num-of-doors, dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['num-of-doors'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "8da9ab34-8cd3-4438-8e71-c4870fb73337",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['num-of-doors'].replace(np.NaN, 'four', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "06837fc7-d2b0-4325-b41d-4d75574e8b27",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "symboling            0\n",
       "normalized-losses    0\n",
       "make                 0\n",
       "fuel-type            0\n",
       "aspiration           0\n",
       "num-of-doors         0\n",
       "body-style           0\n",
       "drive-wheels         0\n",
       "engine-location      0\n",
       "wheel-base           0\n",
       "length               0\n",
       "width                0\n",
       "height               0\n",
       "curb-weight          0\n",
       "engine-type          0\n",
       "num-of-cylinders     0\n",
       "engine-size          0\n",
       "fuel-system          0\n",
       "bore                 0\n",
       "stroke               0\n",
       "compression-ratio    0\n",
       "horsepower           0\n",
       "peak-rpm             0\n",
       "city-mpg             0\n",
       "highway-mpg          0\n",
       "price                0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# agora podemos ver que não existe mais valores missing no nosso conjunto de dados\n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "1d5b5a92-a9e7-4e9d-a214-0cb2935d7ce2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>symboling</th>\n",
       "      <th>normalized-losses</th>\n",
       "      <th>make</th>\n",
       "      <th>fuel-type</th>\n",
       "      <th>aspiration</th>\n",
       "      <th>num-of-doors</th>\n",
       "      <th>body-style</th>\n",
       "      <th>drive-wheels</th>\n",
       "      <th>engine-location</th>\n",
       "      <th>wheel-base</th>\n",
       "      <th>...</th>\n",
       "      <th>engine-size</th>\n",
       "      <th>fuel-system</th>\n",
       "      <th>bore</th>\n",
       "      <th>stroke</th>\n",
       "      <th>compression-ratio</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>peak-rpm</th>\n",
       "      <th>city-mpg</th>\n",
       "      <th>highway-mpg</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>122.0</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>13495</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3</td>\n",
       "      <td>122.0</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>16500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>122.0</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>hatchback</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>94.5</td>\n",
       "      <td>...</td>\n",
       "      <td>152</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>2.68</td>\n",
       "      <td>3.47</td>\n",
       "      <td>9.0</td>\n",
       "      <td>154</td>\n",
       "      <td>5000</td>\n",
       "      <td>19</td>\n",
       "      <td>26</td>\n",
       "      <td>16500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   symboling normalized-losses         make fuel-type aspiration num-of-doors  \\\n",
       "0          3             122.0  alfa-romero       gas        std          two   \n",
       "1          3             122.0  alfa-romero       gas        std          two   \n",
       "2          1             122.0  alfa-romero       gas        std          two   \n",
       "\n",
       "    body-style drive-wheels engine-location  wheel-base  ...  engine-size  \\\n",
       "0  convertible          rwd           front        88.6  ...          130   \n",
       "1  convertible          rwd           front        88.6  ...          130   \n",
       "2    hatchback          rwd           front        94.5  ...          152   \n",
       "\n",
       "   fuel-system  bore  stroke compression-ratio horsepower  peak-rpm city-mpg  \\\n",
       "0         mpfi  3.47    2.68               9.0        111      5000       21   \n",
       "1         mpfi  3.47    2.68               9.0        111      5000       21   \n",
       "2         mpfi  2.68    3.47               9.0        154      5000       19   \n",
       "\n",
       "  highway-mpg  price  \n",
       "0          27  13495  \n",
       "1          27  16500  \n",
       "2          26  16500  \n",
       "\n",
       "[3 rows x 26 columns]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "ae3423db-a3d2-4fdf-8eaa-6c2f8f351278",
   "metadata": {},
   "outputs": [],
   "source": [
    "# vamos agora deixar os atributos do nosso dataset como os tipo apropriados\n",
    "df[['normalized-losses']] = df[['normalized-losses']].astype('int')\n",
    "df[['bore','stroke']] = df[['bore','stroke']].astype('float')\n",
    "df[['horsepower', 'peak-rpm']] = df[['horsepower', 'peak-rpm']].astype('int')\n",
    "df[['price']] = df[['price']].astype('float')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "dd742c00-04f8-45c4-a183-134931d60a1b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "symboling              int64\n",
       "normalized-losses      int32\n",
       "make                  object\n",
       "fuel-type             object\n",
       "aspiration            object\n",
       "num-of-doors          object\n",
       "body-style            object\n",
       "drive-wheels          object\n",
       "engine-location       object\n",
       "wheel-base           float64\n",
       "length               float64\n",
       "width                float64\n",
       "height               float64\n",
       "curb-weight            int64\n",
       "engine-type           object\n",
       "num-of-cylinders      object\n",
       "engine-size            int64\n",
       "fuel-system           object\n",
       "bore                 float64\n",
       "stroke               float64\n",
       "compression-ratio    float64\n",
       "horsepower             int32\n",
       "peak-rpm               int32\n",
       "city-mpg               int64\n",
       "highway-mpg            int64\n",
       "price                float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# visualizando as atualizações\n",
    "df.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "abfc2996-c6e4-4ce9-909a-cd7a667258cd",
   "metadata": {},
   "source": [
    "### Normalização dos dados"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8f1385f0-80e1-43ef-ae74-37b4a60de089",
   "metadata": {},
   "source": [
    "Utilizamos aqui a técnica *Simple feature scaling*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "511dbe09-8a49-457f-918c-83310cd4c440",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['length'] = df['length'] / df['length'].max()\n",
    "df['width'] = df['width'] / df['width'].max()\n",
    "df['height'] = df['height'] / df['height'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "7c2b0828-0b13-4b62-a6a1-1353d18212e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>length</th>\n",
       "      <th>width</th>\n",
       "      <th>height</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.811148</td>\n",
       "      <td>0.890278</td>\n",
       "      <td>0.816054</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.811148</td>\n",
       "      <td>0.890278</td>\n",
       "      <td>0.816054</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.822681</td>\n",
       "      <td>0.909722</td>\n",
       "      <td>0.876254</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.848630</td>\n",
       "      <td>0.919444</td>\n",
       "      <td>0.908027</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.848630</td>\n",
       "      <td>0.922222</td>\n",
       "      <td>0.908027</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     length     width    height\n",
       "0  0.811148  0.890278  0.816054\n",
       "1  0.811148  0.890278  0.816054\n",
       "2  0.822681  0.909722  0.876254\n",
       "3  0.848630  0.919444  0.908027\n",
       "4  0.848630  0.922222  0.908027"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['length','width','height']].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "a82002e7-e701-49f0-b98c-83027be7f2fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>symboling</th>\n",
       "      <th>normalized-losses</th>\n",
       "      <th>wheel-base</th>\n",
       "      <th>length</th>\n",
       "      <th>width</th>\n",
       "      <th>height</th>\n",
       "      <th>curb-weight</th>\n",
       "      <th>engine-size</th>\n",
       "      <th>bore</th>\n",
       "      <th>stroke</th>\n",
       "      <th>compression-ratio</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>peak-rpm</th>\n",
       "      <th>city-mpg</th>\n",
       "      <th>highway-mpg</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>201.000000</td>\n",
       "      <td>201.00000</td>\n",
       "      <td>201.000000</td>\n",
       "      <td>201.000000</td>\n",
       "      <td>201.000000</td>\n",
       "      <td>201.000000</td>\n",
       "      <td>201.000000</td>\n",
       "      <td>201.000000</td>\n",
       "      <td>201.000000</td>\n",
       "      <td>201.000000</td>\n",
       "      <td>201.000000</td>\n",
       "      <td>201.000000</td>\n",
       "      <td>201.000000</td>\n",
       "      <td>201.000000</td>\n",
       "      <td>201.000000</td>\n",
       "      <td>201.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.840796</td>\n",
       "      <td>122.00000</td>\n",
       "      <td>98.797015</td>\n",
       "      <td>0.837102</td>\n",
       "      <td>0.915126</td>\n",
       "      <td>0.899108</td>\n",
       "      <td>2555.666667</td>\n",
       "      <td>126.875622</td>\n",
       "      <td>3.330711</td>\n",
       "      <td>3.256904</td>\n",
       "      <td>10.164279</td>\n",
       "      <td>103.393035</td>\n",
       "      <td>5117.582090</td>\n",
       "      <td>25.179104</td>\n",
       "      <td>30.686567</td>\n",
       "      <td>13207.129353</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.254802</td>\n",
       "      <td>31.99625</td>\n",
       "      <td>6.066366</td>\n",
       "      <td>0.059213</td>\n",
       "      <td>0.029187</td>\n",
       "      <td>0.040933</td>\n",
       "      <td>517.296727</td>\n",
       "      <td>41.546834</td>\n",
       "      <td>0.268072</td>\n",
       "      <td>0.316048</td>\n",
       "      <td>4.004965</td>\n",
       "      <td>37.365623</td>\n",
       "      <td>478.113182</td>\n",
       "      <td>6.423220</td>\n",
       "      <td>6.815150</td>\n",
       "      <td>7947.066342</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-2.000000</td>\n",
       "      <td>65.00000</td>\n",
       "      <td>86.600000</td>\n",
       "      <td>0.678039</td>\n",
       "      <td>0.837500</td>\n",
       "      <td>0.799331</td>\n",
       "      <td>1488.000000</td>\n",
       "      <td>61.000000</td>\n",
       "      <td>2.540000</td>\n",
       "      <td>2.070000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>48.000000</td>\n",
       "      <td>4150.000000</td>\n",
       "      <td>13.000000</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>5118.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>101.00000</td>\n",
       "      <td>94.500000</td>\n",
       "      <td>0.801538</td>\n",
       "      <td>0.890278</td>\n",
       "      <td>0.869565</td>\n",
       "      <td>2169.000000</td>\n",
       "      <td>98.000000</td>\n",
       "      <td>3.150000</td>\n",
       "      <td>3.110000</td>\n",
       "      <td>8.600000</td>\n",
       "      <td>70.000000</td>\n",
       "      <td>4800.000000</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>25.000000</td>\n",
       "      <td>7775.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>122.00000</td>\n",
       "      <td>97.000000</td>\n",
       "      <td>0.832292</td>\n",
       "      <td>0.909722</td>\n",
       "      <td>0.904682</td>\n",
       "      <td>2414.000000</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>3.310000</td>\n",
       "      <td>3.290000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>95.000000</td>\n",
       "      <td>5117.000000</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>10295.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>2.000000</td>\n",
       "      <td>137.00000</td>\n",
       "      <td>102.400000</td>\n",
       "      <td>0.881788</td>\n",
       "      <td>0.925000</td>\n",
       "      <td>0.928094</td>\n",
       "      <td>2926.000000</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>3.580000</td>\n",
       "      <td>3.410000</td>\n",
       "      <td>9.400000</td>\n",
       "      <td>116.000000</td>\n",
       "      <td>5500.000000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>34.000000</td>\n",
       "      <td>16500.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>256.00000</td>\n",
       "      <td>120.900000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>4066.000000</td>\n",
       "      <td>326.000000</td>\n",
       "      <td>3.940000</td>\n",
       "      <td>4.170000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>262.000000</td>\n",
       "      <td>6600.000000</td>\n",
       "      <td>49.000000</td>\n",
       "      <td>54.000000</td>\n",
       "      <td>45400.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        symboling  normalized-losses  wheel-base      length       width  \\\n",
       "count  201.000000          201.00000  201.000000  201.000000  201.000000   \n",
       "mean     0.840796          122.00000   98.797015    0.837102    0.915126   \n",
       "std      1.254802           31.99625    6.066366    0.059213    0.029187   \n",
       "min     -2.000000           65.00000   86.600000    0.678039    0.837500   \n",
       "25%      0.000000          101.00000   94.500000    0.801538    0.890278   \n",
       "50%      1.000000          122.00000   97.000000    0.832292    0.909722   \n",
       "75%      2.000000          137.00000  102.400000    0.881788    0.925000   \n",
       "max      3.000000          256.00000  120.900000    1.000000    1.000000   \n",
       "\n",
       "           height  curb-weight  engine-size        bore      stroke  \\\n",
       "count  201.000000   201.000000   201.000000  201.000000  201.000000   \n",
       "mean     0.899108  2555.666667   126.875622    3.330711    3.256904   \n",
       "std      0.040933   517.296727    41.546834    0.268072    0.316048   \n",
       "min      0.799331  1488.000000    61.000000    2.540000    2.070000   \n",
       "25%      0.869565  2169.000000    98.000000    3.150000    3.110000   \n",
       "50%      0.904682  2414.000000   120.000000    3.310000    3.290000   \n",
       "75%      0.928094  2926.000000   141.000000    3.580000    3.410000   \n",
       "max      1.000000  4066.000000   326.000000    3.940000    4.170000   \n",
       "\n",
       "       compression-ratio  horsepower     peak-rpm    city-mpg  highway-mpg  \\\n",
       "count         201.000000  201.000000   201.000000  201.000000   201.000000   \n",
       "mean           10.164279  103.393035  5117.582090   25.179104    30.686567   \n",
       "std             4.004965   37.365623   478.113182    6.423220     6.815150   \n",
       "min             7.000000   48.000000  4150.000000   13.000000    16.000000   \n",
       "25%             8.600000   70.000000  4800.000000   19.000000    25.000000   \n",
       "50%             9.000000   95.000000  5117.000000   24.000000    30.000000   \n",
       "75%             9.400000  116.000000  5500.000000   30.000000    34.000000   \n",
       "max            23.000000  262.000000  6600.000000   49.000000    54.000000   \n",
       "\n",
       "              price  \n",
       "count    201.000000  \n",
       "mean   13207.129353  \n",
       "std     7947.066342  \n",
       "min     5118.000000  \n",
       "25%     7775.000000  \n",
       "50%    10295.000000  \n",
       "75%    16500.000000  \n",
       "max    45400.000000  "
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "53767c15-0393-47ac-83ea-61bd44b14c42",
   "metadata": {},
   "source": [
    "### Binning"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ffae3983-4e35-46d2-9b5c-7ea1c08eec5c",
   "metadata": {},
   "source": [
    "Aplicando a técnica de binning a coluna 'horsepower'. está técnica consiste em categorizar variáveis númericas continuas\n",
    "para melhor análise"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "137f9a5b-dd47-41bb-80c5-5d6be9ab2248",
   "metadata": {},
   "outputs": [],
   "source": [
    "# convertendo os dados para o tipo int\n",
    "df['horsepower'] = df['horsepower'].astype(int,copy=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "e168a64f-ad7d-4da1-9555-4942d55c6b42",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# gerando um histograma\n",
    "%matplotlib inline\n",
    "plt.hist(df['horsepower'])\n",
    "plt.title('Horsepower bins')\n",
    "plt.xlabel('Horsepower')\n",
    "plt.ylabel('Count')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "3baea471-55ac-4ca7-91c9-ddbb1327d0b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 48.        , 119.33333333, 190.66666667, 262.        ])"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# criando a matriz de bins\n",
    "bins = np.linspace(min(df['horsepower']), max(df['horsepower']), 4)\n",
    "bins"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "4109fa21-16dc-4563-b794-bf09ea1758ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "# primeiro a definição dos grupos, em seguida aplicamos a técnica com o método cut do pandas \n",
    "group_name = ['Low','Medium','High']\n",
    "df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_name,\n",
    "                                 include_lowest=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "e942f3af-e800-4f73-9cd8-0322895f9449",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>horsepower</th>\n",
       "      <th>horsepower-binned</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>111</td>\n",
       "      <td>Low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>111</td>\n",
       "      <td>Low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>154</td>\n",
       "      <td>Medium</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>102</td>\n",
       "      <td>Low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>115</td>\n",
       "      <td>Low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>110</td>\n",
       "      <td>Low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>110</td>\n",
       "      <td>Low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>110</td>\n",
       "      <td>Low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>140</td>\n",
       "      <td>Medium</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>101</td>\n",
       "      <td>Low</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    horsepower horsepower-binned\n",
       "0          111               Low\n",
       "1          111               Low\n",
       "2          154            Medium\n",
       "3          102               Low\n",
       "4          115               Low\n",
       "5          110               Low\n",
       "6          110               Low\n",
       "7          110               Low\n",
       "8          140            Medium\n",
       "10         101               Low"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# visualiando o resultado\n",
    "df[['horsepower', 'horsepower-binned']].head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "5a2b4d24-dafe-4291-8335-bf9e438032bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Low       153\n",
       "Medium     43\n",
       "High        5\n",
       "Name: horsepower-binned, dtype: int64"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# a contagem por grupos\n",
    "df['horsepower-binned'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "68b64fbc-7c69-4d70-afdc-e4ae66231335",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# gerando um gráfico de barras\n",
    "plt.bar(group_name, df['horsepower-binned'].value_counts())\n",
    "plt.title('Horsepower Binned')\n",
    "plt.ylabel('Count')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "31c66438-5d8c-48e8-8f81-8d2c4cd82403",
   "metadata": {},
   "source": [
    "### Dummy Variable"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ed8c56e2-c631-46c9-8110-83a81d342434",
   "metadata": {},
   "source": [
    "Aplicando a variável fictícia para rotular as categorias das colunas 'fuel-type' e 'aspiration'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "3b53426e-9f56-4e2c-9630-d480ecd780df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>fuel-type-diesel</th>\n",
       "      <th>fuel-type-gas</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   fuel-type-diesel  fuel-type-gas\n",
       "0                 0              1\n",
       "1                 0              1\n",
       "2                 0              1\n",
       "3                 0              1\n",
       "4                 0              1"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# usando o método get_dummies do pandas para gerar as variáveis fictícia\n",
    "dummy = pd.get_dummies(df['fuel-type'])\n",
    "dummy.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)\n",
    "dummy.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "df81e970-79a0-4c3a-a3ea-8c134857d8bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# fazendo uma junção das variáveis fictícias com o dataframe e dropando a coluna 'fuel-type'\n",
    "df = pd.concat([df,dummy], axis=1)\n",
    "df.drop('fuel-type', axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "07b84e7c-fa6f-4e0d-ac01-61148481ac01",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>aspiration-std</th>\n",
       "      <th>aspiration-turbo</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   aspiration-std  aspiration-turbo\n",
       "0               1                 0\n",
       "1               1                 0\n",
       "2               1                 0\n",
       "3               1                 0\n",
       "4               1                 0"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# processo igual para a coluna 'aspiration'\n",
    "dummy1 = pd.get_dummies(df['aspiration'])\n",
    "dummy1.rename(columns={'std':'aspiration-std', 'turbo':'aspiration-turbo'},inplace=True)\n",
    "dummy1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "91337712-da7c-4b9c-93ff-2d12af342d98",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.concat([df, dummy1], axis=1)\n",
    "df.drop('aspiration',axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "6f368752-d1d6-4c00-83ec-c8368e3a514f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>symboling</th>\n",
       "      <th>normalized-losses</th>\n",
       "      <th>make</th>\n",
       "      <th>num-of-doors</th>\n",
       "      <th>body-style</th>\n",
       "      <th>drive-wheels</th>\n",
       "      <th>engine-location</th>\n",
       "      <th>wheel-base</th>\n",
       "      <th>length</th>\n",
       "      <th>width</th>\n",
       "      <th>...</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>peak-rpm</th>\n",
       "      <th>city-mpg</th>\n",
       "      <th>highway-mpg</th>\n",
       "      <th>price</th>\n",
       "      <th>horsepower-binned</th>\n",
       "      <th>fuel-type-diesel</th>\n",
       "      <th>fuel-type-gas</th>\n",
       "      <th>aspiration-std</th>\n",
       "      <th>aspiration-turbo</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>122</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>0.811148</td>\n",
       "      <td>0.890278</td>\n",
       "      <td>...</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>13495.0</td>\n",
       "      <td>Low</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3</td>\n",
       "      <td>122</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>0.811148</td>\n",
       "      <td>0.890278</td>\n",
       "      <td>...</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>16500.0</td>\n",
       "      <td>Low</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>122</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>two</td>\n",
       "      <td>hatchback</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>94.5</td>\n",
       "      <td>0.822681</td>\n",
       "      <td>0.909722</td>\n",
       "      <td>...</td>\n",
       "      <td>154</td>\n",
       "      <td>5000</td>\n",
       "      <td>19</td>\n",
       "      <td>26</td>\n",
       "      <td>16500.0</td>\n",
       "      <td>Medium</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3 rows × 29 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   symboling  normalized-losses         make num-of-doors   body-style  \\\n",
       "0          3                122  alfa-romero          two  convertible   \n",
       "1          3                122  alfa-romero          two  convertible   \n",
       "2          1                122  alfa-romero          two    hatchback   \n",
       "\n",
       "  drive-wheels engine-location  wheel-base    length     width  ...  \\\n",
       "0          rwd           front        88.6  0.811148  0.890278  ...   \n",
       "1          rwd           front        88.6  0.811148  0.890278  ...   \n",
       "2          rwd           front        94.5  0.822681  0.909722  ...   \n",
       "\n",
       "   horsepower  peak-rpm city-mpg highway-mpg    price horsepower-binned  \\\n",
       "0         111      5000       21          27  13495.0               Low   \n",
       "1         111      5000       21          27  16500.0               Low   \n",
       "2         154      5000       19          26  16500.0            Medium   \n",
       "\n",
       "   fuel-type-diesel  fuel-type-gas  aspiration-std  aspiration-turbo  \n",
       "0                 0              1               1                 0  \n",
       "1                 0              1               1                 0  \n",
       "2                 0              1               1                 0  \n",
       "\n",
       "[3 rows x 29 columns]"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# método head para visualizar o df\n",
    "df.head(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c96ee3d0-116d-43c6-bae6-b12791e7256b",
   "metadata": {},
   "source": [
    "## EDA - Análise exploratória de dados"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "72e57c7f-e746-4dd7-bcf5-63d475f59198",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "symboling               int64\n",
      "normalized-losses       int32\n",
      "make                   object\n",
      "num-of-doors           object\n",
      "body-style             object\n",
      "drive-wheels           object\n",
      "engine-location        object\n",
      "wheel-base            float64\n",
      "length                float64\n",
      "width                 float64\n",
      "height                float64\n",
      "curb-weight             int64\n",
      "engine-type            object\n",
      "num-of-cylinders       object\n",
      "engine-size             int64\n",
      "fuel-system            object\n",
      "bore                  float64\n",
      "stroke                float64\n",
      "compression-ratio     float64\n",
      "horsepower              int32\n",
      "peak-rpm                int32\n",
      "city-mpg                int64\n",
      "highway-mpg             int64\n",
      "price                 float64\n",
      "horsepower-binned    category\n",
      "fuel-type-diesel        uint8\n",
      "fuel-type-gas           uint8\n",
      "aspiration-std          uint8\n",
      "aspiration-turbo        uint8\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "# visualizando os tipos de dados que temos para poder trabalhar da análise\n",
    "print(df.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "ea097506-1559-44bc-9cdb-ef6dc0531111",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>symboling</th>\n",
       "      <th>normalized-losses</th>\n",
       "      <th>wheel-base</th>\n",
       "      <th>length</th>\n",
       "      <th>width</th>\n",
       "      <th>height</th>\n",
       "      <th>curb-weight</th>\n",
       "      <th>engine-size</th>\n",
       "      <th>bore</th>\n",
       "      <th>stroke</th>\n",
       "      <th>compression-ratio</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>peak-rpm</th>\n",
       "      <th>city-mpg</th>\n",
       "      <th>highway-mpg</th>\n",
       "      <th>price</th>\n",
       "      <th>fuel-type-diesel</th>\n",
       "      <th>fuel-type-gas</th>\n",
       "      <th>aspiration-std</th>\n",
       "      <th>aspiration-turbo</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>symboling</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.466264</td>\n",
       "      <td>-0.535987</td>\n",
       "      <td>-0.365404</td>\n",
       "      <td>-0.242423</td>\n",
       "      <td>-0.550160</td>\n",
       "      <td>-0.233118</td>\n",
       "      <td>-0.110581</td>\n",
       "      <td>-0.139896</td>\n",
       "      <td>-0.007992</td>\n",
       "      <td>-0.182196</td>\n",
       "      <td>0.075776</td>\n",
       "      <td>0.279718</td>\n",
       "      <td>-0.035527</td>\n",
       "      <td>0.036233</td>\n",
       "      <td>-0.082391</td>\n",
       "      <td>-0.196735</td>\n",
       "      <td>0.196735</td>\n",
       "      <td>0.054615</td>\n",
       "      <td>-0.054615</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>normalized-losses</th>\n",
       "      <td>0.466264</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.056661</td>\n",
       "      <td>0.019424</td>\n",
       "      <td>0.086802</td>\n",
       "      <td>-0.373737</td>\n",
       "      <td>0.099404</td>\n",
       "      <td>0.112360</td>\n",
       "      <td>-0.029800</td>\n",
       "      <td>0.055127</td>\n",
       "      <td>-0.114713</td>\n",
       "      <td>0.217300</td>\n",
       "      <td>0.239544</td>\n",
       "      <td>-0.225016</td>\n",
       "      <td>-0.181877</td>\n",
       "      <td>0.133999</td>\n",
       "      <td>-0.101546</td>\n",
       "      <td>0.101546</td>\n",
       "      <td>0.006911</td>\n",
       "      <td>-0.006911</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>wheel-base</th>\n",
       "      <td>-0.535987</td>\n",
       "      <td>-0.056661</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.876024</td>\n",
       "      <td>0.814507</td>\n",
       "      <td>0.590742</td>\n",
       "      <td>0.782097</td>\n",
       "      <td>0.572027</td>\n",
       "      <td>0.493203</td>\n",
       "      <td>0.157964</td>\n",
       "      <td>0.250313</td>\n",
       "      <td>0.371297</td>\n",
       "      <td>-0.360227</td>\n",
       "      <td>-0.470606</td>\n",
       "      <td>-0.543304</td>\n",
       "      <td>0.584642</td>\n",
       "      <td>0.307237</td>\n",
       "      <td>-0.307237</td>\n",
       "      <td>-0.256889</td>\n",
       "      <td>0.256889</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>length</th>\n",
       "      <td>-0.365404</td>\n",
       "      <td>0.019424</td>\n",
       "      <td>0.876024</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.857170</td>\n",
       "      <td>0.492063</td>\n",
       "      <td>0.880665</td>\n",
       "      <td>0.685025</td>\n",
       "      <td>0.608941</td>\n",
       "      <td>0.123913</td>\n",
       "      <td>0.159733</td>\n",
       "      <td>0.579688</td>\n",
       "      <td>-0.286040</td>\n",
       "      <td>-0.665192</td>\n",
       "      <td>-0.698142</td>\n",
       "      <td>0.690628</td>\n",
       "      <td>0.211187</td>\n",
       "      <td>-0.211187</td>\n",
       "      <td>-0.230085</td>\n",
       "      <td>0.230085</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>width</th>\n",
       "      <td>-0.242423</td>\n",
       "      <td>0.086802</td>\n",
       "      <td>0.814507</td>\n",
       "      <td>0.857170</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.306002</td>\n",
       "      <td>0.866201</td>\n",
       "      <td>0.729436</td>\n",
       "      <td>0.544879</td>\n",
       "      <td>0.188814</td>\n",
       "      <td>0.189867</td>\n",
       "      <td>0.614972</td>\n",
       "      <td>-0.245856</td>\n",
       "      <td>-0.633531</td>\n",
       "      <td>-0.680635</td>\n",
       "      <td>0.751265</td>\n",
       "      <td>0.244356</td>\n",
       "      <td>-0.244356</td>\n",
       "      <td>-0.305732</td>\n",
       "      <td>0.305732</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>height</th>\n",
       "      <td>-0.550160</td>\n",
       "      <td>-0.373737</td>\n",
       "      <td>0.590742</td>\n",
       "      <td>0.492063</td>\n",
       "      <td>0.306002</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.307581</td>\n",
       "      <td>0.074694</td>\n",
       "      <td>0.180327</td>\n",
       "      <td>-0.060822</td>\n",
       "      <td>0.259737</td>\n",
       "      <td>-0.086901</td>\n",
       "      <td>-0.309909</td>\n",
       "      <td>-0.049800</td>\n",
       "      <td>-0.104812</td>\n",
       "      <td>0.135486</td>\n",
       "      <td>0.281578</td>\n",
       "      <td>-0.281578</td>\n",
       "      <td>-0.090336</td>\n",
       "      <td>0.090336</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>curb-weight</th>\n",
       "      <td>-0.233118</td>\n",
       "      <td>0.099404</td>\n",
       "      <td>0.782097</td>\n",
       "      <td>0.880665</td>\n",
       "      <td>0.866201</td>\n",
       "      <td>0.307581</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.849072</td>\n",
       "      <td>0.644041</td>\n",
       "      <td>0.167412</td>\n",
       "      <td>0.156433</td>\n",
       "      <td>0.758001</td>\n",
       "      <td>-0.279349</td>\n",
       "      <td>-0.749543</td>\n",
       "      <td>-0.794889</td>\n",
       "      <td>0.834415</td>\n",
       "      <td>0.221046</td>\n",
       "      <td>-0.221046</td>\n",
       "      <td>-0.321955</td>\n",
       "      <td>0.321955</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>engine-size</th>\n",
       "      <td>-0.110581</td>\n",
       "      <td>0.112360</td>\n",
       "      <td>0.572027</td>\n",
       "      <td>0.685025</td>\n",
       "      <td>0.729436</td>\n",
       "      <td>0.074694</td>\n",
       "      <td>0.849072</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.572516</td>\n",
       "      <td>0.205806</td>\n",
       "      <td>0.028889</td>\n",
       "      <td>0.822636</td>\n",
       "      <td>-0.256755</td>\n",
       "      <td>-0.650546</td>\n",
       "      <td>-0.679571</td>\n",
       "      <td>0.872335</td>\n",
       "      <td>0.070779</td>\n",
       "      <td>-0.070779</td>\n",
       "      <td>-0.110040</td>\n",
       "      <td>0.110040</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>bore</th>\n",
       "      <td>-0.139896</td>\n",
       "      <td>-0.029800</td>\n",
       "      <td>0.493203</td>\n",
       "      <td>0.608941</td>\n",
       "      <td>0.544879</td>\n",
       "      <td>0.180327</td>\n",
       "      <td>0.644041</td>\n",
       "      <td>0.572516</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.055390</td>\n",
       "      <td>0.001250</td>\n",
       "      <td>0.566786</td>\n",
       "      <td>-0.267344</td>\n",
       "      <td>-0.582121</td>\n",
       "      <td>-0.591390</td>\n",
       "      <td>0.543154</td>\n",
       "      <td>0.054435</td>\n",
       "      <td>-0.054435</td>\n",
       "      <td>-0.227782</td>\n",
       "      <td>0.227782</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>stroke</th>\n",
       "      <td>-0.007992</td>\n",
       "      <td>0.055127</td>\n",
       "      <td>0.157964</td>\n",
       "      <td>0.123913</td>\n",
       "      <td>0.188814</td>\n",
       "      <td>-0.060822</td>\n",
       "      <td>0.167412</td>\n",
       "      <td>0.205806</td>\n",
       "      <td>-0.055390</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.187854</td>\n",
       "      <td>0.097598</td>\n",
       "      <td>-0.063745</td>\n",
       "      <td>-0.034079</td>\n",
       "      <td>-0.034741</td>\n",
       "      <td>0.082267</td>\n",
       "      <td>0.241033</td>\n",
       "      <td>-0.241033</td>\n",
       "      <td>-0.218190</td>\n",
       "      <td>0.218190</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>compression-ratio</th>\n",
       "      <td>-0.182196</td>\n",
       "      <td>-0.114713</td>\n",
       "      <td>0.250313</td>\n",
       "      <td>0.159733</td>\n",
       "      <td>0.189867</td>\n",
       "      <td>0.259737</td>\n",
       "      <td>0.156433</td>\n",
       "      <td>0.028889</td>\n",
       "      <td>0.001250</td>\n",
       "      <td>0.187854</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.214392</td>\n",
       "      <td>-0.435716</td>\n",
       "      <td>0.331425</td>\n",
       "      <td>0.268465</td>\n",
       "      <td>0.071107</td>\n",
       "      <td>0.985231</td>\n",
       "      <td>-0.985231</td>\n",
       "      <td>-0.307522</td>\n",
       "      <td>0.307522</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>horsepower</th>\n",
       "      <td>0.075776</td>\n",
       "      <td>0.217300</td>\n",
       "      <td>0.371297</td>\n",
       "      <td>0.579688</td>\n",
       "      <td>0.614972</td>\n",
       "      <td>-0.086901</td>\n",
       "      <td>0.758001</td>\n",
       "      <td>0.822636</td>\n",
       "      <td>0.566786</td>\n",
       "      <td>0.097598</td>\n",
       "      <td>-0.214392</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.107882</td>\n",
       "      <td>-0.822102</td>\n",
       "      <td>-0.804592</td>\n",
       "      <td>0.809729</td>\n",
       "      <td>-0.168941</td>\n",
       "      <td>0.168941</td>\n",
       "      <td>-0.251284</td>\n",
       "      <td>0.251284</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>peak-rpm</th>\n",
       "      <td>0.279718</td>\n",
       "      <td>0.239544</td>\n",
       "      <td>-0.360227</td>\n",
       "      <td>-0.286040</td>\n",
       "      <td>-0.245856</td>\n",
       "      <td>-0.309909</td>\n",
       "      <td>-0.279349</td>\n",
       "      <td>-0.256755</td>\n",
       "      <td>-0.267344</td>\n",
       "      <td>-0.063745</td>\n",
       "      <td>-0.435716</td>\n",
       "      <td>0.107882</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.115354</td>\n",
       "      <td>-0.058606</td>\n",
       "      <td>-0.101536</td>\n",
       "      <td>-0.475755</td>\n",
       "      <td>0.475755</td>\n",
       "      <td>0.189976</td>\n",
       "      <td>-0.189976</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>city-mpg</th>\n",
       "      <td>-0.035527</td>\n",
       "      <td>-0.225016</td>\n",
       "      <td>-0.470606</td>\n",
       "      <td>-0.665192</td>\n",
       "      <td>-0.633531</td>\n",
       "      <td>-0.049800</td>\n",
       "      <td>-0.749543</td>\n",
       "      <td>-0.650546</td>\n",
       "      <td>-0.582121</td>\n",
       "      <td>-0.034079</td>\n",
       "      <td>0.331425</td>\n",
       "      <td>-0.822102</td>\n",
       "      <td>-0.115354</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.972044</td>\n",
       "      <td>-0.686571</td>\n",
       "      <td>0.265676</td>\n",
       "      <td>-0.265676</td>\n",
       "      <td>0.189237</td>\n",
       "      <td>-0.189237</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>highway-mpg</th>\n",
       "      <td>0.036233</td>\n",
       "      <td>-0.181877</td>\n",
       "      <td>-0.543304</td>\n",
       "      <td>-0.698142</td>\n",
       "      <td>-0.680635</td>\n",
       "      <td>-0.104812</td>\n",
       "      <td>-0.794889</td>\n",
       "      <td>-0.679571</td>\n",
       "      <td>-0.591390</td>\n",
       "      <td>-0.034741</td>\n",
       "      <td>0.268465</td>\n",
       "      <td>-0.804592</td>\n",
       "      <td>-0.058606</td>\n",
       "      <td>0.972044</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.704692</td>\n",
       "      <td>0.198690</td>\n",
       "      <td>-0.198690</td>\n",
       "      <td>0.241851</td>\n",
       "      <td>-0.241851</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>price</th>\n",
       "      <td>-0.082391</td>\n",
       "      <td>0.133999</td>\n",
       "      <td>0.584642</td>\n",
       "      <td>0.690628</td>\n",
       "      <td>0.751265</td>\n",
       "      <td>0.135486</td>\n",
       "      <td>0.834415</td>\n",
       "      <td>0.872335</td>\n",
       "      <td>0.543154</td>\n",
       "      <td>0.082267</td>\n",
       "      <td>0.071107</td>\n",
       "      <td>0.809729</td>\n",
       "      <td>-0.101536</td>\n",
       "      <td>-0.686571</td>\n",
       "      <td>-0.704692</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.110326</td>\n",
       "      <td>-0.110326</td>\n",
       "      <td>-0.179578</td>\n",
       "      <td>0.179578</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>fuel-type-diesel</th>\n",
       "      <td>-0.196735</td>\n",
       "      <td>-0.101546</td>\n",
       "      <td>0.307237</td>\n",
       "      <td>0.211187</td>\n",
       "      <td>0.244356</td>\n",
       "      <td>0.281578</td>\n",
       "      <td>0.221046</td>\n",
       "      <td>0.070779</td>\n",
       "      <td>0.054435</td>\n",
       "      <td>0.241033</td>\n",
       "      <td>0.985231</td>\n",
       "      <td>-0.168941</td>\n",
       "      <td>-0.475755</td>\n",
       "      <td>0.265676</td>\n",
       "      <td>0.198690</td>\n",
       "      <td>0.110326</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-1.000000</td>\n",
       "      <td>-0.408228</td>\n",
       "      <td>0.408228</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>fuel-type-gas</th>\n",
       "      <td>0.196735</td>\n",
       "      <td>0.101546</td>\n",
       "      <td>-0.307237</td>\n",
       "      <td>-0.211187</td>\n",
       "      <td>-0.244356</td>\n",
       "      <td>-0.281578</td>\n",
       "      <td>-0.221046</td>\n",
       "      <td>-0.070779</td>\n",
       "      <td>-0.054435</td>\n",
       "      <td>-0.241033</td>\n",
       "      <td>-0.985231</td>\n",
       "      <td>0.168941</td>\n",
       "      <td>0.475755</td>\n",
       "      <td>-0.265676</td>\n",
       "      <td>-0.198690</td>\n",
       "      <td>-0.110326</td>\n",
       "      <td>-1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.408228</td>\n",
       "      <td>-0.408228</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>aspiration-std</th>\n",
       "      <td>0.054615</td>\n",
       "      <td>0.006911</td>\n",
       "      <td>-0.256889</td>\n",
       "      <td>-0.230085</td>\n",
       "      <td>-0.305732</td>\n",
       "      <td>-0.090336</td>\n",
       "      <td>-0.321955</td>\n",
       "      <td>-0.110040</td>\n",
       "      <td>-0.227782</td>\n",
       "      <td>-0.218190</td>\n",
       "      <td>-0.307522</td>\n",
       "      <td>-0.251284</td>\n",
       "      <td>0.189976</td>\n",
       "      <td>0.189237</td>\n",
       "      <td>0.241851</td>\n",
       "      <td>-0.179578</td>\n",
       "      <td>-0.408228</td>\n",
       "      <td>0.408228</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>aspiration-turbo</th>\n",
       "      <td>-0.054615</td>\n",
       "      <td>-0.006911</td>\n",
       "      <td>0.256889</td>\n",
       "      <td>0.230085</td>\n",
       "      <td>0.305732</td>\n",
       "      <td>0.090336</td>\n",
       "      <td>0.321955</td>\n",
       "      <td>0.110040</td>\n",
       "      <td>0.227782</td>\n",
       "      <td>0.218190</td>\n",
       "      <td>0.307522</td>\n",
       "      <td>0.251284</td>\n",
       "      <td>-0.189976</td>\n",
       "      <td>-0.189237</td>\n",
       "      <td>-0.241851</td>\n",
       "      <td>0.179578</td>\n",
       "      <td>0.408228</td>\n",
       "      <td>-0.408228</td>\n",
       "      <td>-1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   symboling  normalized-losses  wheel-base    length  \\\n",
       "symboling           1.000000           0.466264   -0.535987 -0.365404   \n",
       "normalized-losses   0.466264           1.000000   -0.056661  0.019424   \n",
       "wheel-base         -0.535987          -0.056661    1.000000  0.876024   \n",
       "length             -0.365404           0.019424    0.876024  1.000000   \n",
       "width              -0.242423           0.086802    0.814507  0.857170   \n",
       "height             -0.550160          -0.373737    0.590742  0.492063   \n",
       "curb-weight        -0.233118           0.099404    0.782097  0.880665   \n",
       "engine-size        -0.110581           0.112360    0.572027  0.685025   \n",
       "bore               -0.139896          -0.029800    0.493203  0.608941   \n",
       "stroke             -0.007992           0.055127    0.157964  0.123913   \n",
       "compression-ratio  -0.182196          -0.114713    0.250313  0.159733   \n",
       "horsepower          0.075776           0.217300    0.371297  0.579688   \n",
       "peak-rpm            0.279718           0.239544   -0.360227 -0.286040   \n",
       "city-mpg           -0.035527          -0.225016   -0.470606 -0.665192   \n",
       "highway-mpg         0.036233          -0.181877   -0.543304 -0.698142   \n",
       "price              -0.082391           0.133999    0.584642  0.690628   \n",
       "fuel-type-diesel   -0.196735          -0.101546    0.307237  0.211187   \n",
       "fuel-type-gas       0.196735           0.101546   -0.307237 -0.211187   \n",
       "aspiration-std      0.054615           0.006911   -0.256889 -0.230085   \n",
       "aspiration-turbo   -0.054615          -0.006911    0.256889  0.230085   \n",
       "\n",
       "                      width    height  curb-weight  engine-size      bore  \\\n",
       "symboling         -0.242423 -0.550160    -0.233118    -0.110581 -0.139896   \n",
       "normalized-losses  0.086802 -0.373737     0.099404     0.112360 -0.029800   \n",
       "wheel-base         0.814507  0.590742     0.782097     0.572027  0.493203   \n",
       "length             0.857170  0.492063     0.880665     0.685025  0.608941   \n",
       "width              1.000000  0.306002     0.866201     0.729436  0.544879   \n",
       "height             0.306002  1.000000     0.307581     0.074694  0.180327   \n",
       "curb-weight        0.866201  0.307581     1.000000     0.849072  0.644041   \n",
       "engine-size        0.729436  0.074694     0.849072     1.000000  0.572516   \n",
       "bore               0.544879  0.180327     0.644041     0.572516  1.000000   \n",
       "stroke             0.188814 -0.060822     0.167412     0.205806 -0.055390   \n",
       "compression-ratio  0.189867  0.259737     0.156433     0.028889  0.001250   \n",
       "horsepower         0.614972 -0.086901     0.758001     0.822636  0.566786   \n",
       "peak-rpm          -0.245856 -0.309909    -0.279349    -0.256755 -0.267344   \n",
       "city-mpg          -0.633531 -0.049800    -0.749543    -0.650546 -0.582121   \n",
       "highway-mpg       -0.680635 -0.104812    -0.794889    -0.679571 -0.591390   \n",
       "price              0.751265  0.135486     0.834415     0.872335  0.543154   \n",
       "fuel-type-diesel   0.244356  0.281578     0.221046     0.070779  0.054435   \n",
       "fuel-type-gas     -0.244356 -0.281578    -0.221046    -0.070779 -0.054435   \n",
       "aspiration-std    -0.305732 -0.090336    -0.321955    -0.110040 -0.227782   \n",
       "aspiration-turbo   0.305732  0.090336     0.321955     0.110040  0.227782   \n",
       "\n",
       "                     stroke  compression-ratio  horsepower  peak-rpm  \\\n",
       "symboling         -0.007992          -0.182196    0.075776  0.279718   \n",
       "normalized-losses  0.055127          -0.114713    0.217300  0.239544   \n",
       "wheel-base         0.157964           0.250313    0.371297 -0.360227   \n",
       "length             0.123913           0.159733    0.579688 -0.286040   \n",
       "width              0.188814           0.189867    0.614972 -0.245856   \n",
       "height            -0.060822           0.259737   -0.086901 -0.309909   \n",
       "curb-weight        0.167412           0.156433    0.758001 -0.279349   \n",
       "engine-size        0.205806           0.028889    0.822636 -0.256755   \n",
       "bore              -0.055390           0.001250    0.566786 -0.267344   \n",
       "stroke             1.000000           0.187854    0.097598 -0.063745   \n",
       "compression-ratio  0.187854           1.000000   -0.214392 -0.435716   \n",
       "horsepower         0.097598          -0.214392    1.000000  0.107882   \n",
       "peak-rpm          -0.063745          -0.435716    0.107882  1.000000   \n",
       "city-mpg          -0.034079           0.331425   -0.822102 -0.115354   \n",
       "highway-mpg       -0.034741           0.268465   -0.804592 -0.058606   \n",
       "price              0.082267           0.071107    0.809729 -0.101536   \n",
       "fuel-type-diesel   0.241033           0.985231   -0.168941 -0.475755   \n",
       "fuel-type-gas     -0.241033          -0.985231    0.168941  0.475755   \n",
       "aspiration-std    -0.218190          -0.307522   -0.251284  0.189976   \n",
       "aspiration-turbo   0.218190           0.307522    0.251284 -0.189976   \n",
       "\n",
       "                   city-mpg  highway-mpg     price  fuel-type-diesel  \\\n",
       "symboling         -0.035527     0.036233 -0.082391         -0.196735   \n",
       "normalized-losses -0.225016    -0.181877  0.133999         -0.101546   \n",
       "wheel-base        -0.470606    -0.543304  0.584642          0.307237   \n",
       "length            -0.665192    -0.698142  0.690628          0.211187   \n",
       "width             -0.633531    -0.680635  0.751265          0.244356   \n",
       "height            -0.049800    -0.104812  0.135486          0.281578   \n",
       "curb-weight       -0.749543    -0.794889  0.834415          0.221046   \n",
       "engine-size       -0.650546    -0.679571  0.872335          0.070779   \n",
       "bore              -0.582121    -0.591390  0.543154          0.054435   \n",
       "stroke            -0.034079    -0.034741  0.082267          0.241033   \n",
       "compression-ratio  0.331425     0.268465  0.071107          0.985231   \n",
       "horsepower        -0.822102    -0.804592  0.809729         -0.168941   \n",
       "peak-rpm          -0.115354    -0.058606 -0.101536         -0.475755   \n",
       "city-mpg           1.000000     0.972044 -0.686571          0.265676   \n",
       "highway-mpg        0.972044     1.000000 -0.704692          0.198690   \n",
       "price             -0.686571    -0.704692  1.000000          0.110326   \n",
       "fuel-type-diesel   0.265676     0.198690  0.110326          1.000000   \n",
       "fuel-type-gas     -0.265676    -0.198690 -0.110326         -1.000000   \n",
       "aspiration-std     0.189237     0.241851 -0.179578         -0.408228   \n",
       "aspiration-turbo  -0.189237    -0.241851  0.179578          0.408228   \n",
       "\n",
       "                   fuel-type-gas  aspiration-std  aspiration-turbo  \n",
       "symboling               0.196735        0.054615         -0.054615  \n",
       "normalized-losses       0.101546        0.006911         -0.006911  \n",
       "wheel-base             -0.307237       -0.256889          0.256889  \n",
       "length                 -0.211187       -0.230085          0.230085  \n",
       "width                  -0.244356       -0.305732          0.305732  \n",
       "height                 -0.281578       -0.090336          0.090336  \n",
       "curb-weight            -0.221046       -0.321955          0.321955  \n",
       "engine-size            -0.070779       -0.110040          0.110040  \n",
       "bore                   -0.054435       -0.227782          0.227782  \n",
       "stroke                 -0.241033       -0.218190          0.218190  \n",
       "compression-ratio      -0.985231       -0.307522          0.307522  \n",
       "horsepower              0.168941       -0.251284          0.251284  \n",
       "peak-rpm                0.475755        0.189976         -0.189976  \n",
       "city-mpg               -0.265676        0.189237         -0.189237  \n",
       "highway-mpg            -0.198690        0.241851         -0.241851  \n",
       "price                  -0.110326       -0.179578          0.179578  \n",
       "fuel-type-diesel       -1.000000       -0.408228          0.408228  \n",
       "fuel-type-gas           1.000000        0.408228         -0.408228  \n",
       "aspiration-std          0.408228        1.000000         -1.000000  \n",
       "aspiration-turbo       -0.408228       -1.000000          1.000000  "
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# obtendo a correlação geral dos dados\n",
    "df.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "77e8a935-63d8-4b92-aae3-999abf34afec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>normalized-losses</th>\n",
       "      <th>wheel-base</th>\n",
       "      <th>length</th>\n",
       "      <th>width</th>\n",
       "      <th>height</th>\n",
       "      <th>curb-weight</th>\n",
       "      <th>engine-size</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>normalized-losses</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.056661</td>\n",
       "      <td>0.019424</td>\n",
       "      <td>0.086802</td>\n",
       "      <td>-0.373737</td>\n",
       "      <td>0.099404</td>\n",
       "      <td>0.112360</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>wheel-base</th>\n",
       "      <td>-0.056661</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.876024</td>\n",
       "      <td>0.814507</td>\n",
       "      <td>0.590742</td>\n",
       "      <td>0.782097</td>\n",
       "      <td>0.572027</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>length</th>\n",
       "      <td>0.019424</td>\n",
       "      <td>0.876024</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.857170</td>\n",
       "      <td>0.492063</td>\n",
       "      <td>0.880665</td>\n",
       "      <td>0.685025</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>width</th>\n",
       "      <td>0.086802</td>\n",
       "      <td>0.814507</td>\n",
       "      <td>0.857170</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.306002</td>\n",
       "      <td>0.866201</td>\n",
       "      <td>0.729436</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>height</th>\n",
       "      <td>-0.373737</td>\n",
       "      <td>0.590742</td>\n",
       "      <td>0.492063</td>\n",
       "      <td>0.306002</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.307581</td>\n",
       "      <td>0.074694</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>curb-weight</th>\n",
       "      <td>0.099404</td>\n",
       "      <td>0.782097</td>\n",
       "      <td>0.880665</td>\n",
       "      <td>0.866201</td>\n",
       "      <td>0.307581</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.849072</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>engine-size</th>\n",
       "      <td>0.112360</td>\n",
       "      <td>0.572027</td>\n",
       "      <td>0.685025</td>\n",
       "      <td>0.729436</td>\n",
       "      <td>0.074694</td>\n",
       "      <td>0.849072</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   normalized-losses  wheel-base    length     width  \\\n",
       "normalized-losses           1.000000   -0.056661  0.019424  0.086802   \n",
       "wheel-base                 -0.056661    1.000000  0.876024  0.814507   \n",
       "length                      0.019424    0.876024  1.000000  0.857170   \n",
       "width                       0.086802    0.814507  0.857170  1.000000   \n",
       "height                     -0.373737    0.590742  0.492063  0.306002   \n",
       "curb-weight                 0.099404    0.782097  0.880665  0.866201   \n",
       "engine-size                 0.112360    0.572027  0.685025  0.729436   \n",
       "\n",
       "                     height  curb-weight  engine-size  \n",
       "normalized-losses -0.373737     0.099404     0.112360  \n",
       "wheel-base         0.590742     0.782097     0.572027  \n",
       "length             0.492063     0.880665     0.685025  \n",
       "width              0.306002     0.866201     0.729436  \n",
       "height             1.000000     0.307581     0.074694  \n",
       "curb-weight        0.307581     1.000000     0.849072  \n",
       "engine-size        0.074694     0.849072     1.000000  "
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# correlação entre algumas colunas\n",
    "cor = df[['normalized-losses','wheel-base','length','width','height','curb-weight','engine-size']]\n",
    "cor.corr()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e73105eb-a4f1-4552-a661-f4ea76ec6e06",
   "metadata": {},
   "source": [
    "### Variáveis Númericas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "26b4cef6-4202-4a0e-804e-512124732fec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# observando relação linear entre o coluna 'engine-size' e 'price'\n",
    "sns.regplot(x='engine-size', y='price', data=df)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "c42afbfd-dd7b-48da-92c8-04549359774b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>engine-size</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>engine-size</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.872335</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>price</th>\n",
       "      <td>0.872335</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             engine-size     price\n",
       "engine-size     1.000000  0.872335\n",
       "price           0.872335  1.000000"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['engine-size','price']].corr()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3505d373-8832-40b7-ae30-370809d10cee",
   "metadata": {},
   "source": [
    "Podemos visualizar pelo gráfico de regressão que a medida que motor aumenta o preço também aumenta. indicando uma correlação direta e positiva entre essas variáveis. 'engine-size' parece ser uma boa preditora, já que a linha de regressão é quase perfeita. \n",
    "> A correlaçao entre as duas é de aproximadamente 0.87"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "7fedb5bd-d399-4654-a9f7-0cf1e141e796",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZoAAAEGCAYAAABcolNbAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAABDNklEQVR4nO3deXicd3nv//c9m2a0y5a8xEtsx1t2QhxnIcQuUJJAD3BoAKfnQHoKTQ6lP2hPaRO6AIe2V5OWlpLS0qRAgVCWNMCVnEISEozthDhxnA3HibfI+ybJkq1lNOtz//54nhmNxiNpZM1oRtL9yqVL0ne2r0bO89F3F1XFGGOMKRdfpStgjDFmerOgMcYYU1YWNMYYY8rKgsYYY0xZWdAYY4wpq0ClK1BtWltbdcmSJZWuhjHGTCkvvPBCl6q2FbrNgibPkiVL2L59e6WrYYwxU4qIHBzpNus6M8YYU1YWNMYYY8rKgsYYY0xZWdAYY4wpKwsaY4wxZWVBk2fXiT5uvf9ZNu3qqHRVjDFmWrCgyRPwCR19MT77yE4LG2OMKQELmgJqQwGCfuG+Le2Vrooxxkx5FjQjiAT9HOmJVroaxhgz5VnQjGAwmWZhS22lq2GMMVOeBU0B0USKZFq544Zlla6KMcZMebbXWZ60o8xpCHPHDctYv3pOpatjjDFTngVNnlXzGvje7ddUuhrGGDNtWNeZMcaYsrKgMcYYU1YWNMYYY8rKgsYYY0xZWdAYY4wpKwsaY4wxZWVBY4wxpqxsHc00tmlXB/dtaedwT5RFLbW2CNUYUxHWoskzXc6j2bSrg88+spOOvhjNkaAdfWCMqRgLmjzT5Tya+7a0E/QLtaEAImJHHxhjKsaCpoDpcFE+3BMlEvQPK7OjD4wxlVDxoBERv4i8JCL/5X0/S0SeEJG93ueWnPt+RkT2ichuEbkxp/xKEdnh3XaviIhXXiMiP/DKnxORJcXWa6pflBe11DKYTA8rs6MPjDGVUPGgAT4FvJ7z/V3Az1V1BfBz73tE5CJgA3AxcBPwLyKS+ZP9q8DtwArv4yav/KNAj6ouB74E3FNspab6RfmOG5aRTCvRRApVtaMPjDEVU9GgEZGFwLuBr+UUvxf4lvf1t4D35ZR/X1Xjqrof2AesFZH5QKOqblVVBb6d95jMcz0EvD3T2hnNdLgor189hy+852LmNIQ5M5hkTkOYL7znYpt1ZoyZdJWe3vyPwJ8ADTllc1X1OICqHheRzJVxAfBszv2OeGVJ7+v88sxjDnvPlRKRM8BsoCu3EiJyO26LiJrmOdPmPJr1q+dM+Z/BGDP1VSxoROQ3gA5VfUFE1hfzkAJlOkr5aI8ZXqB6P3A/wJo1a9TOozHGmNKpZIvmLcB7RORdQBhoFJHvACdFZL7XmpkPZOYYHwEW5Tx+IXDMK19YoDz3MUdEJAA0Ad3l+oGMMcacrWJjNKr6GVVdqKpLcAf5N6rq/wQeAW7z7nYb8LD39SPABm8m2VLcQf9tXjdbn4hc442/fCTvMZnnusV7jbNaNMYYY8qn0mM0hdwNPCgiHwUOAR8AUNWdIvIg8BqQAj6hqpn5ux8HvglEgEe9D4CvAw+IyD7clsyGyfohjDHGuMT+wB9uzZo1un379kpXwxhjphQReUFV1xS6rRrW0RhjjJnGLGiMMcaUVTWO0ZgpyI4kMMaMxIKmSk2lC3fmSIKgX4YdSfAFqNo6G2Mmj3WdVaGpdpaMHUlgjBmNBU0VmmoXbjuSwBgzGus6G4fJ6s463BOlORIcVlbNF+5FLbV09MWoDQ39c5rqu18bY0rHWjRFKmV31qZdHdx6/7Ncf8/GgsdGT7WzZOxIAmPMaCxoilSq7qxiAmuqXbjtSAJjzGis66xIxXZnjdW9lhtY4B4bHU2kuG9Le/Z+61fP4QvefY/0RFlY5bPOwI4kMMaMzIKmSMWMQxQzzbfYwLILtzFmurCusyIV051VTPfaVBt/McaYibKgKVIx4xCHe6Kk0g7tnf3sOtFLe2c/qbQzrLUy1cZfjDFmoqzrbBzG6s5qqAmwt6Mfv0/w+4SUoxw9HWPFnPphzzHVxl+KMZV2MjDGTC4LmhLKHrmQOXlB88o90238xbagMcaMxrrOSqg/kWZBc5iAX0irEvALC5rDDCTSYz94CptqOxkYYyaXtWhKKDMzbVnbUFdZNJFiTkO4grUqv6m2k4ExZnJZi6aEZupAv82kM8aMxoKmhGbqCvk7blhG72CSvSf7eP34Gfae7KN3MDntA9YYUxzrOiuxYgb6p+MMLQUQEBGQofkQxhhjLZpJNtXOminGfVvaaYoEWTGngdXzGlkxp4GmSNAmAxhjAAuaSTcdZ2gVs1DVGDNzWdBMsul4SFhDTYCjp2OkHB22ULW+xnpmjTEWNJNuOs7QGrZQNfPB2QtVjTEzkwXNJJvMKdBjHbBWKjN1oaoxpjgWNJNssqZAT+akg0UttQT8Ppa11bN6XiPL2uoJ+H1TupVmjCkd60SvgMnY66yYA9ZK5Y4blvHZR3YSTaSIBP0MJtMzYqGqMaY4FWvRiEhYRLaJyCsislNE/q9XPktEnhCRvd7nlpzHfEZE9onIbhG5Maf8ShHZ4d12r4iIV14jIj/wyp8TkSWT/oNWyGROOpipC1WNMcWpZIsmDrxNVftFJAg8LSKPAu8Hfq6qd4vIXcBdwJ0ichGwAbgYOA94UkRWqmoa+CpwO/As8FPgJuBR4KNAj6ouF5ENwD3Ahyb3x6yMYk4ELaXptiO1MaZ0KtaiUVe/923Q+1DgvcC3vPJvAe/zvn4v8H1VjavqfmAfsFZE5gONqrpV3WlO3857TOa5HgLenmntTHczdd81Y0z1qehkABHxi8jLQAfwhKo+B8xV1eMA3ufMn8kLgMM5Dz/ilS3wvs4vH/YYVU0BZ4DZBepxu4hsF5HtnZ2dJfrpKsu6s4wx1aKikwG8bq83iUgz8GMRuWSUuxdqiego5aM9Jr8e9wP3A6xZs2baLP6w7ixjTDWoiunNqnoa2IQ7tnLS6w7D+5yZj3sEWJTzsIXAMa98YYHyYY8RkQDQBHSX42cwxhhTWCVnnbV5LRlEJAK8A9gFPALc5t3tNuBh7+tHgA3eTLKlwApgm9e91ici13jjLx/Je0zmuW4BNqotVy+LyVocaoyZeirZdTYf+JaI+HED70FV/S8R2Qo8KCIfBQ4BHwBQ1Z0i8iDwGpACPuF1vQF8HPgmEMGdbfaoV/514AER2YfbktkwKT/ZDLNpVweffugV+uMp0o7S1R/n0w+9whdvudy67owxiP2BP9yaNWt0+/btla7GlHLTlzazr3MAvwgioAppVZa31fHYH66rdPWMMZNARF5Q1TWFbquKMZpq4qjSH0/ZhpDjsP9UFJ+AzyeICD6f4BO33BhjbAuaPI5CR28Mv09oCAdpDAcI+C2PjTHmXNkVdARpRzkdTXCoO8rJ3hjRRKrSVapay1rrcNRtDSqKo4qjbrkxxljQFGEgnuLEmRiHu6OciSZJO9atluvOm1bTUhtEgFTaQYCW2iB33rS60lUzxlQBC5pxSKYdTg3EOdQdpaMvRixp562AuzD07265nCsWtzC/KcIVi1v4O5txZozx2BjNOVBV+mMp+mMpQgEfDeEgDTUBfL4ZsY1aQbYLgTFmJBY0E5RIOZzqj9MzkKCuJkBjJEBNwD/2A40xZoawoCkRR5W+WJK+WJKaoJ+GcID60Mxp5Wza1cF9W9o53BNlUUstd9ywzFo4xhjAxmjKIp5M09XnjuV09ceJp6b3WM5kHhttjJl6LGjyxJLpki3WdFTpHUxytGeQY6cH6Yslp+VC0Nxjo0Xcz0G/cN+W9kpXzRhTBSxo8uzvGuAj33ierz3Vzt6TfSULhlgyTafXyjnVHyeZdkryvNVgMo+NNsZMPTZGU8DR04N8d9thvrvtMOc1h1m3so11K9tYMaeeiR7QmXaUM4NJzgwmiYT8NIaD1Ib8E37eSlrUUsuBU/30DqZIpB1Cfh+NkQBLZtdXumrGmCpgQZNnWWsd7796MZv3dHKkZ5Bjp2N8b9thvleG0BlMpBlMpAn4fNSHA1N2u5trl81i24Fud78zgUTaoaMvwa1Xzap01YwxVcB2b87zpjdfqT96fDOqSnvXAJv3dLJ5dyeHewaH3e+85jA3rGhj/arShE5GbcidIr2tvXvKzOK69f5n2d/VT19sqEXTEA6wtLWe791+TaWrZ4yZBKPt3mxBkycTNLlUlf1e6GwqEDrzm8LcsKKV9avmsHLuxENnW3s3927cSyjgoy7kJ5ZySKaVL7zn4qoMm+vv2UhzJDjs51Z1uwifuvNtFayZMWayjBY01nVWBBFhWVs9y9rq+e3rlmRDZ/OeLg51Rzl+JsYPth/hB9uPMK8xzLqVraxb1caquQ3nFDrff/4wfp8Q8vtIOkrQ78PRNPdtaa/KoFnUUktHX4za0NA/p8FkmoUttRWslTGmWljQjFN+6Bw4FWXT7o5s6JzoHR46N6xsZf04Q+d47yCNYe9X4+2KHPAJB7r6OR1N0BAO4q+ihaB33LCMzz6yk2giRSToZzCZJplW7rhhWaWrZoypAhY0EyAiLG2tY2nr0mzobN7dyaY9ndnQeXD7ER7MCZ11K9tYPW/00JnfGOHUQHzYlOFY0mFuY4TugQQ90SR1IT8N4SCRUOW3u1m/eg63HDnN157ez0AiTV3Iz8euX1qVrS9jzOSzMZo8hcZozsX+rgE27+5k855ODnYPX08yt7EmO5GgUOhsa+/myxv3EvAJ4aCPWNIh5SifetsK1i4bPpMr6PfRGA5SHw5UrJWT2Rkg6JdhLZrxjinZNjbGTF02GWAcShU0ufZ3DbBljxs6B/KON57TUJOdMn3h/KHQ2dbezfefP8yJ3kHmNUbYcNWis0Iml4hQV+OuywkHJ7eVc+v9z541RhNNpJjTEC561lmpwsoYUxk2GWAcfCLU1QSIJdMlO+DM7V6r47brlnDg1FBL58CpKB19cf7zhSP85wtHmNNQ447prJzDVUtbRg2WfLlHF9QE/TSGA9TXBCZlIejhnijNkeCwsvHuDHDflnaS6TSn+ocv+qzWCRDGmOJZ0OTxCcxtDAPutjGxZJpoIk085ZRkO5ols+tYcp0bOgdPDc1e2981QEdfnIdeOMpDLxzNho7b0mnEN47AiCfTdCbTnOpPUB8O0BAe+eiCUnRXlWLW2d6OPs5Ek/h8gt8npBylqy9BMt03rroYY6qPdZ3lWbNmjW7fvv2scsdRYil3JX80kS75XmWHTkXddTp7OtnfNTDstrb6muzstfGGTkbm6IKGnFZOKcdWJvo8l33+cQaT7i4JGSnHIRL086vP3zi+H9YYM+lsjGYcRgqafKm0w2Ay7X4kStfNBkOhs3lPJ+0jhM66lW1cdN74Q8cn4m13E+S2b2yb8NhKRqZldKQnysJzaBld+Zc/ozeWwocgAqrgoDSFA2z/i3dm73fvk3vOmt32yXesHFddjTGlZ2M0ZRDw+2jwu8c4A8RzWjux5MTOn1k8u5YPX3s+H772fA51R7NjOu1dA3T2x/nhi0f54YtHaa0PccPKNtaPI3QyRxf0DibZf6qflkgIVc22cs511+WJHuW8cm5jgW1sgixtHdqY894n9/DljfvwCQR8bvfclzfuA7CwMaaKWdCUSE3AT03AT3Ot282W29qZSDfb4ll5oZNp6XQO0NWf4EcvHuVH5xg68xq89TohP35xx0YqtaI/s+hzXlNgxEWfX3t6vxcybveaT9zuta89vd+CxpgqZkFTBj6fO3OtrsZ9e1Nph2gyTcxr8Tjn2F25eFYtH77mfD58zfkczgmdNwqFjrdOZ7TQ2XDVIr68cS+DiTThoI/+uENald++9vxz/tnP1frVc/gCjNr9NpBIE8jb3NonbrkxpnpVbIxGRBYB3wbmAQ5wv6p+WURmAT8AlgAHgA+qao/3mM8AHwXSwCdV9XGv/Ergm0AE+CnwKVVVEanxXuNK4BTwIVU9MFq9ih2jOVeqSjzlEE2kiSZSJFITn1RwpMcLnd1d7OvsH3bbbC901q1s5ZIFTWeFzkjrdQI+dwfmhio6usAmDBhTvUoyRiMi5wMrVPVJEYkAAVWdyNzTFPBHqvqiiDQAL4jIE8BvAz9X1btF5C7gLuBOEbkI2ABcDJwHPCkiK1U1DXwVuB14FjdobgIexQ2lHlVdLiIbgHuAD02gzhMmIoSDfsJBP7PqQiVp7SxsqeV/XH0+/+Pq8znSE2XLni427e5kX2c/p/oT/Pilo/z4paPMrgvx1hXuhp+XnNc0bCeB/FdNOQ490QQ90QS1ITdwMi20SvnY9Uv58sZ9pBwHn4Cj7sfHrl9a0XoZY0ZXVItGRH4X90I+S1UvEJEVwL+q6ttLVhGRh4GveB/rVfW4iMwHNqnqKq81g6r+jXf/x4HP47Z6fqGqq73yW73H35G5j6puFZEAcAJo01F+6HK3aEZT6tbO0Z7B7JTpfR15LZ26ECvnNrD7ZB+1QR+RkH/UrW6A7AFt9TUBQvl9WJPEZp0ZU50mPL1ZRF4G1gLPqeoVXtkOVb20RBVcAmwBLgEOqWpzzm09qtoiIl8BnlXV73jlX8dttRwA7lbVd3jlbwXuVNXfEJFXgZtU9Yh32xvA1aralff6t+MGKYsXL77y4MGDpfixJizT2smcxHmuYzsweuj4fUJ9jbvGBpTW+jD/8KHLR32+cNDvhk4ogM8ntk+ZMTNcKbrO4qqayEyB9VoHJRncEZF64IfAH6hq7yhbphS6QUcpH+0xwwtU7wfuB7dFM1adJ0vA76PR2zTzXFo7mfGX472DzPfGX37r6sXZ0PnmMwdIOUracQ8pOzOYxO8TugcSvHL4NJcsaBpxo87MrgndkuDlQ6f5q5/spD+eJuU4dPXF+eOHXuHvbrncwsYYU3TQbBaRPwUiIvLrwO8B/2+iLy4iQdyQ+Q9V/ZFXfFJE5ud0nXV45UeARTkPXwgc88oXFijPfcwRLxybgO6J1rsS8sd20t4U6mgiRSzhkHKGB8+29m7ueXwXA/EUaUfpGUhwz+MD3HnjatYum8VvXb2Y7Qd6ONk7SDKt9MVTxFMOaUeJOsofPvgKs+pCvHW5uyPBSKHjqHLvxr10DyTJ1CDlOCQHEtzz2K5hQWOtHmNmpmKD5i7cgfUdwB24A+5fm8gLi9t0+Trwuqr+Q85NjwC3AXd7nx/OKf+uiPwD7mSAFcA2VU2LSJ+IXAM8B3wE+Ke859oK3AJsHG18ZirJdHfVewP0iZS7U0HM62q7/6l2ege9vcP8gir0Dia5/6n27PhLZnpzJOSjpS7obsqZSNMYDnL09CDdAwkefuUYD79yjIBPCPqF85oifPT6pVxzwexsXQ6dGiC/fZVW2HtyaK7Ipl0d/PFDr9AXS43Y6rEgmhrs92TGq9igiQDfUNV/AxARv1c2/iXkQ94CfBjY4Y0BAfwpbsA8KCIfBQ4BHwBQ1Z0i8iDwGu6MtU94M84APs7Q9OZHvQ9wg+wBEdmH25LZMIH6VrVQwEco4KPJ20X5SE8Un5CdziwCiHI4Z9X/2mWz+BQrhk1v/pQ3vfn4mUE27+nipzuOc6RnkJSjpBzlja4B/vzhV1m7ZBa3rFnI5QubSY0Q3Sl1t9NpCAe4+9HX6Ym6XXMBvw9V6Ikms62e3P3SmiNBOvpifPaRnXwBpvRFbLpdlKfr78mUV7FB83PgHUBmFDkC/Ay47lxfWFWfpvAYCkDB2Wyq+tfAXxco3447kSC/PIYXVDNNZqzLJzJs1+n8N3ztslkFZ5jNb3LHdLa1d5NOO8O61xyFZ/d38+z+bpojQYTCA3Z+GZom/UbXAIIimf8EVDS7l9t9W9oJ+iW771ptKEA0kSrbMQGTEQDT8aI82b8nMz0UO0c1rKrZqUre15O/T4kp2tLZtaQddQftU042IJbOruW85gjNtSFqijgg7XjvIPXhALPqQpw/q5als2tprQsS9MZrTg8mR5wV0tZQc1aZ4o7rqPeRcbgnOuzoajj3fdfGkgmAjr7YsADYtKtj7AePQ+5FWcT9HPQL921pL+nrTKbJ/D2Z6aPYoBkQkTdnvvFW4g+Wp0qmFN516XzyN5R2FN592XnZCQULmiMsmV3H3MYwjZEgwQI7AMxvjBBLDo3ABP0+IqEAF5/XxHc/djV33LCMmhHW1AzE07x4sIe0oyxqjrgLLB03YNKO4igsag4TS6ZZ1FLLYN5mpOXad22yAmA6XpQn8/dkpo9iu87+APhPEcnM5ppPhVfYm9Ftbe9mbmNN3m7IAba2d/PJnPvl78uW9I4/iMbdiQXZ/dCS7n5omUWdG65axLymMB+6ahEPbN1fsA598RSffuhXNEWCrJrbQEd/nHgqjaPu6zaGgnzsrRdw7PQgv/nmBfzjk3tRTVIbChTcVBOK6/Ia6z6lOBG0GItaajlwqp/eweGnhi6ZXT/2g6tUZvPTaCI14uanxuQrKmhU9XkRWQ2swu3m36WqybLWzEzI4Z4orfU1tDWEs2WqOubFNOj3EcxZuzO3MczXnn6DfZ1Dj1s2OzJsXCc20mwAz5nBJNsODJ9VHvYJ77lsfvZ53nx+C79+4RwefOEIg8lodtV//vToYmaujTUuUooTQYtx7bJZbDvQ7U3KgETaoaMvwa1XFX9Ed7UpZvNTY/KNGjQi8jZV3Sgi78+7aYW4g8w/KvhAU3GluJiKCL/z788NCxmA9lOD/NEPXuLvP3QF4B5SVvDxwHd/92q27OnkJ786zqGeod7WWMrhgecO8fqJPj6wZhGJpMNjr51kVl0o23L6/vYjLG2r58ZL5lET8HPPY7tGnbkG7gUwmU5zqn94KyJ3sHqy/irf2t5NW31ozFblVDPRs4fMzDNWi2YdsBH4bwVuU8CCpkqV6mK6dX9PwfKXjvSyoCVCLOFQV+MnmkijOrRVg4jbHTW3McwH1ixi6xvdJB2HVFrpi6WIeZMTth3oYduBHvw+IRzwuV1aSrbO33j6AJcsaCIU8PFGZz+qSjKtqLqv4ROGnUK6t6OPM1Fv/ZBPSDlKV1+CZHpoTc9k/VV+rq1KY6abUYNGVT8nIj7gUVV9cJLqZEqg2IvpRKb5Zg57u/2ty/jHn+/F72PYrsofvHJow4bjvYM0hgMIQkttiGTaoS+e4sxgkmTanRwwkEgzkEjjE7zFqH6On3EvyomUg6NKOqf1pN7riAwVJlIO5K0fckTP2rJnMv4qn6wuOmOq3ZhjNKrqiMjvAxY0U8xYF9NSrfPI7J6cu6vy77xlCR+74YLshqDzG73TPL1ZWEG/j0jQz8LmWu66eRX/58FX6OpPkEi7LZ3eWIreWAq/T/i7x3ezflUbI2y7hj+nPOgXBpPu7DaRoW69kH+kJVvlYwPnxriKnd78hIh8WkQWiciszEdZa2bKrpTTfC9b2MzF5zUxvynMxec18aZFLdTXBGhrqGHx7Fp+b/0FOAqxVBrF3actM3ttTmOYT75tBbPrQ8xvCtNaHyLkTbVOO8qjr57gzh/uYKSDNP0iHO6OcjqaYMWcBmbXhQj4hbQqAb8wuy7EirmNE3mrzsn61XP4wnsuZk5DmDODSeY0hPnCey628Q0z4xQ7vfl3cLvffy+v3P40m8JKNc23mJbROy+ZRyjgc7vpugeY3xTh1rWLueL8FlT1rO1wLprfyM2XzKM3nmTz7k5ePdY74uunVEmmHboHErzvTQu49xd7mdNQQ23ITyzlVLQVYQPnxhQfNBfhhsz1uIHzFPCv5aqUmRylGkModluSQhddx1FiKbd77a2r2gpuh/Obb15IZ1+cDfc/W3AXgnhK+dvHdrNuVStvPr+FT/7aUGAtaK7l9huW2sXemAoqNmi+BfQC93rf3+qVfbAclTKlMdZAfzFjCH6gUI9V7nr3ibSMfD43oDIhldk2J+qN7WSOP2hrqHG7w9J61k7RAI/tPMFjO09QXxPgLctn88GrFnLl+S3Z3Q4OnYpW/HRQY2aqYoNmlarmHrn4CxF5pRwVMqVRTHdWMTPTxAeFruySc60u5ewqf95OBfGUu0tBNJlmUXOEg91RgiLZgf60o7TUBlkwq5YdR87QH0/x+M6TPL7zZDZ01q1s48rzW0g5DqejCWqCfl4+2MMDzx7kyOnBabGrsjHVrNigeUlErlHVZwFE5Grgl+Wrlpmo8e6yO9Lafr/Ph6qDQnbtinjlGXfcsIxPP/QKR08PknY0e1bOX7z7ogn/HJkp1C3An7/7Ij79w1eyh7n5fEJTOMgfe4e5neqP89TeLjbt6TwrdOpq/LzlAvcQN8dR/nnTGwR8Ql3Iz4neQf7i4Vf5Sy6Z8WEz3Y41MNWh2KC5GviIiBzyvl8MvC4iOwBV1cvKUjtzzg73RPELtHf2Z1elt9aHhnVnFdPqWdZax96OfgK+4a2IZa11w14vmXaIJ91ASqWVmsDYR03nG+si97aL5vLbx5Zkp1HX+H1suGoR61a3EUs6zK6v4X1XLOB9VyzIhs7mPZ386sgZBuJpfvbaSX722kl8AuGgn+ZIkLSjBH0+0k6af9q4j7XLZhEJ+rPHLMwk0/FYA1Mdig2am8paC1NyDTUB9nb0489ZIX/0dIwVc4Y2dCym1XPnTav55PdepD/hbYYpUB/yc+dNq7PPc89juxiIpwkFfNkwGoinzzrKeTTFXOQ27ergoRePulOmvTGln+w4wdVLZ7NulRs2meOtRwsdRyGacMeBfAJ13uLQIz0DnDgTw++NG9XXBIiExj5KYayfa6q0EOysGVMuxW6qebDcFTGllT3rJdMnpnnlFD+ILz7JLnxUdb/P1d41cNZpnrmHmhWjmIvcfVva6Y8lOT2YzIZecySYvU8k5CcSco9ASGV2oU6k8YlkQ6d7IMEffP9lOvvj2TN6+mIp+mIpfAJ/8+gu1q1sZc35s+iLJQn4fNTW+KmvCRAu4vyeXFOthTBZu1qbmafYFo2ZYvoTaRY0h7Or7UN+H/PqaxjIWfVYzCD+PY/toncwNSyvegdT42qtFKOYi9zOY2fojaXcvdRwQ687mmTnsTNnPV/A76PB76PB24U6lnSIJlIE/T5+/9eW8+WNexHcLr/e2NDJoU+8dpInXjtJXcjPtRfMZv2qNtacP4vewSRBv4/6mgAN4QCBAmf35JtqLQTbMseUiwXNNJW5aCxrG+oqiyZSzMnZ4LGY6c17TvadNVFAvfKMpbNr2dc5gORs++IoLG8t/gJVzEUuG5K5DSplWHgWIiLZ1s5s4P1XLqQhHODrv9zPsdODXDivkXdfOo+BZJrNezp55fBpBhJpnny9gydf70CA5togv3HpefyPaxbTE/URCflpCAepC408njPVWgi2ZY4pFwuaaaqYi0Yx05vTI0xHyy2/6+YL+fRDr9DvzQbz+4TmmiB33XxhSevreEeG5h9LkCkvVijg492Xn8e7Lz/P28wzRTSeZjCZ5j2Xn0dPNMF3th7kJztOkEi7Exx6okkeeO4gD75wmOuXu7PXrloyi3DQn+1ay59EMNVaCHbWjCkXC5ppqtiLxq+OnGbnsTMMJNKcGUzyqyOnx31hWb96Dl+85fIJXaCKqW8k6CeaPLv1kn9c8nj4fUJjOEhjOIjjuHuw1YcDHDgVZW5jDUG/0B9P0x9LEU2miaccfr6rg5/v6qA25OfaZe46nbVLZxEJ+bOTCMJB35RsIdiWOaYcLGimsbEuGvc+uYcvb9yHTyDgc//a/vLGfcDQjsyleq1SPEdtyFcwaGpDw8dLJnLcc2axaEdfjKZwEMUd72mOBEk6Dqf6EyyfU8/Lh08TTaSzoRMJumM661a2sXZJC7U1AS5e0MSfv+tC/v2ZA9ZCMDOaBc0M9rWn93sh416ofQIpx+FrT+/PBk3ILyQK9J9VYtv9vnia/I0KfF55RrHHPY91n8Wz6rLdXgHc7rl42uGCtnq++IHLOR1N8MXHd/Ps/m4cdUN6464ONnqhc82yWaxfNYe1S1q45zcvO+eZa8ZMBxY0M9hAIo0PJZ5KZ1f9+2X44HpDOED3QHLYhAABGsOV+acT8MuwXQnSzvCFofc8tovugQSOd9pn2nFIDiSGzZIr5kjo/G6vmPcefertKzivOcKDzx9ia3v3WRMlBDd0frG7k1/s7syGzrpVbVy9ZBZ1NUFqa/zUhSa+RseYqcKCZgarCfiIJtLuJC5vtlhSh3dFrZzbyP6u/rPOvV/aWj/i85ZLMbPb9nX0k9ah46RRd+LCvo7+7H2KWfcz1pjRt7ceKrhtT8gv/P7bVrB5TycvHuoZFjo+gUvOa+L9Vy7g6iWzqK1xNxNtCFtLZyRTacGrGZkFzQw2KxIgmki7F0wdXp6R+ct+XlOg4gPaxcxuS2WmpGV69rywSeVPVRuHQo8sNFYEEE8r733TAt592Xx+8XoHf//kHga999hR+NXRM/zq6BnCQd+wiQT1NUHqatzJBOGgb0ZugZNvqi14NSOr6H7pIvINEekQkVdzymaJyBMistf73JJz22dEZJ+I7BaRG3PKrxSRHd5t94r3f6mI1IjID7zy50RkyaT+gNXO56OtPpg9Itkn0FYfRHK6pqrplMjM7LYrFrUwrzHMFYta+GLOuAoMHeusOvSRWw5uyyhzHMFgMk0smSbtKEtnD7WMNu3q4NMPvcJLh3s42RvjpcM9fPqhV9i0q2PMei6eXcv8pgjff/4Q8WSagF8I+ofXIZZ0+MXuTj7//17j/f/yDJ99+FUeeeUY+7v6OXgqSkdvjP54atxTt6eTUp4Aayqr0i2abwJfAb6dU3YX8HNVvVtE7vK+v1NELgI2ABcD5wFPishKVU0DXwVuB54Ffoq7N9ujwEeBHlVdLiIbgHuAD03KTzYFZNZ5zGsausDmL+qE6pryOlZdlrfVs+tkf8HyjHddOp9/eHJv9nvF7V5716Xzs2V3P/o6PTljPam0kkwluPvR14t6LyIhP4d6BvGJe9Q0CD4/+Bx3Xc4fvmMlm/Z08uKh08RSDpv2dLJpTyfhgI+rvZbO1ctmeWf1+L2PAH7fzGnpTLUFr2ZkFQ0aVd1SoJXxXmC99/W3gE3AnV7591U1DuwXkX3AWhE5ADSq6lYAEfk28D7coHkv8HnvuR4CviIiojqBfpRpZCqu8xjLuy6dz+6Te8+avJAbIo++eiLTozbsPo++eiI7225f58DQWI93n7TCG53F798G7q4E2W4w75+dT4SbL53PzZfOp3cwyQNbD/Kz107SF08RSzls3tPJ5hFCJxz0URsMUFvjzx7qNl0taqmtmvFBMzGVbtEUMldVjwOo6nERyfz5uAC3xZJxxCtLel/nl2cec9h7rpSInAFmA125Lygit+O2iFi8eHFJf5hqVsqV4NUyaFtUiHT0F9xWJ3fCQDqzC0He/VLj6MoqNHlBES5orWPxrFoGEmleOtjDxt0dxNNpt2tNQBAc1WGhUxPwcfWyWaxfOYervaMMQgFftsUzHScTXLtsFtsOdHsTNyCRdujsT/Bba88+7ttUt2oMmpEU6jPQUcpHe8zwAtX7gfsB1qxZM6NaO6XoFqumQdt9Hf04kJ1Jh7rrbnJDJDlCWOSW+3ySDZtcvnF0Xd1184UFj1i46+YLCfh9NEV8/NtT7fREk0MP8mZmnN8S4YNrF7N5TycvHOwhnnLYsqeLLXu6ckKnjauXzSYSdFs3tSE/ddNorc7W9m7mNIToHRxq0TRGAmxt7+aTla6cGZdqDJqTIjLfa83MBzKjr0eARTn3Wwgc88oXFijPfcwREQkATUB3OSs/E1XTLsWlmnUW8guDBYIms1B1dm2QU7kB4ZldO3xMoVDLKdeejrPHkwAO9Qxy8yXzuPmSefTFkvxy36mRQ2fpLNatbOOaZbOJhPzZ83TqavxT+hC3wz1RZtfV0Fo/NGaoqjZGMwVVY9A8AtwG3O19fjin/Lsi8g+4kwFWANtUNS0ifSJyDfAc8BHgn/KeaytwC7DRxmdKr5oGbf0CqZzZZrnl41Eb8hNPOV5319C6nDpvkeUNK1v58cvHz3rcDStbs1/f/ejrDCYdgr6hA+EGk86wCQUj9cQpMKcxTH8shYhw0yXzuMkLnWfecENn+wEvdPZ2sWWvGzprvdC51gsdESESdHeuznS3TRVTbVNSM7KKBo2IfA934L9VRI4An8MNmAdF5KPAIeADAKq6U0QeBF4DUsAnvBlnAB/HncEWwZ0E8KhX/nXgAW/iQDfurDVTYtV0QVjeVs+ek+4YTDYgGD7rrBhjLVT96Y4TBR/30x0n+JL3r2z/qag7vuDLWRjqKPtPFRfA9TXuBp1pR+mPpeiNJWkIB7nx4nncePE8+mMpnnmji005ofPU3i6e2ttFKOBj7RIvdC5wJxJsa+/mB9sPc6I3xqKWWj6+bhm/duHccb0vk2k6TlaZqSo96+zWEW56+wj3/2vgrwuUbwcuKVAewwsqUz7VdEHIHRfJbKuTGRcZj7EWqsZHOD8hvzyVVhLpocWdPiAYGF/zyu8TmmqDNNUGiSXT9MVSDMRT1IcDvPPiebzTC50Hnj3I4ztP0BtLkUg5PL2vi6f3uaGzoq2efZ19xFNu/Y6fifHa8TP85Xsu4W0XzaUu5C/qMLfJVG3HFtz75B6+9vR+BhJp6kJ+Pnb90rM2ny3mPjNRNXadmSmm2i4IoaCfkKPZ3QNC5zA4vn71HG45cvqsi8Z4fqaGGj9dqeF7sTle+bkKB90ZZq31Ifrj7hHUsWSa14718vS+LpoiQVrrQ5yOJhlIpEk5SiLlsPN471nP1R9Pc8/ju7h8cTOncM/p+Y+tB/nOcweJJp2quFBWyxquYnY6L+Vu6NONBY0piWq5INy3pZ2mSJD5TZFs2blMTNi0q4OHXjxKW0MNi70WzUMvHuWyhc1FP0804YyrfDxEhIZwkIZwkETK4U9e/BVBvxAOuCHWWl9DXTJNcyTEuy+fz92P7ir4PCd64/z89ZNce8FsHnjmCN/cejA7YaE3luJLT+5FVfnUr6+acJ2nsmJ2Oi/mPjOVBY2ZVko1MeG+Le0k02lO9Q+fWjuewIqnHYI+d6Fn7u7Y8fTEgyZXKODjRG+M5kgQVUir4jhKOOijsz/GOy+aO2LQAPz1T3cR9LvTuQvNkvvq5nY+tPZ8amv81Aarr4ttMgwk0uTPo/Dl7XRezH1KpVrWrRXLgsZMK4taajlwqv+stRdLZg9NBsjMAMuXOwt4b0cfZ6JJfD7B7xNSjtLVlyCZ7gPccZNC62xyt4ipC7ktoZqcC3PKcagrwzqX3AkZPgT1Kf3x1LCW3UiCfiE50pndQCzlEE2kiCZS3v192S1xZsoGoJnfZe4yKkeHZiEWe59SqKZ1a8WaeX+amGnt2mWz6OhLkEg72dXkHX0Jrl02tJp8QVO44GNzyxMpB7yjBARxjxQQr5yRD37LLf/Y9Utx1A0XRx3vs1teanfcsIxkWokmUqi6R1I73vk580b4eTN+9PHr+LN3rR71Pk+8dpL+uBs0ybTDmcEkx88McuBUlBNnYpwZTJIscUutGJt2dXDr/c9y/T0bufX+Z4va9PRcFPO7nKzfd7VtNpr5HQTbllw60n0saMy0srW9m7b6ECG/D0ch5PfRVh9ia/vQOt2/et+lNNb4h+1a3Vjj56/eN/T/SdALDMdR1OuKgqEgqQ25j89dF+qT4X+9fvIdK/nU25YTCfpJOW4X3qfetnxYf/1IbYHxthFG22U7d9p5IXU1Ad4+xjTnv3l0F7/51Wf40x/v4Gc5oaPqhtup/jiHu6Mc7o7S2RdnYBJ2ns6clPrSoR5OnBnkpUM9/HGRO2yPVzG/y2LuUwqHe6JE8lrFlVq3lmlddfTFQJ3USPezrjMzrRzuidJaX0Nbw8irydevnsO9t7551FlyhdfRBLPraIo9EO6T71g56oUm4INkgYbAuayrLOeEjEz32rPt3Tzb3k3QL1x5fgvrV7Zx3QWt1HsnribTDsm0Q1/M3TWhJuguFK0N+akJlLabrZiTUktprN9lsfeZqGpat5a/K8hILGjMtFLs/4RjXZTHWkdTqgPhGiNBTg2cvZVNU96Ehony4U6tzifArLoQfbER/xgF4Me/dx1b3+hm855Oth3oJpFysqET8O1hzZKzQwcgnkwTT6Y5HXW7ISMhd5eC2qCff/nFvgmtOSnmpNTpqJrWrRWafFOIBY2ZVkr1P+FYa4NKtXZoso7Kfu+b5hfcMud9b5pPc22I5trQqI+vDQV4+4VzePuFc3hqdyffeOYAJ3pjJFIOKUfPCp11K9t4S17oOKoMxN3Fpg88c+CsqdT/+HP3jKDcsJlqs6smQzWtWyv0h10hFjRmWinH/4QjjTSUoquqlEdlj3ZRPtGboDkSoDeWyu4k3RgOcKI3Ma7X2Nbezb8+1U7AJyyeFSGaSDMQT7OgJcLejv6zWjpXnt/C+lVnh873nj981vvqKHx10xt8/NeWE/T7xpxdVegYBkdheev03wttstatjRX0uX/YjcaCxkw7U+nog1IF41j1Pew9d+4YSf7Y1bVLW9i6v+es575yURMigqry/ecPE/BJdjC6LhTAJ0LQ5+PHH7+O5/afYtOeTp5r7yaecnhufzfP7R8KnXUr23jL8tnEUoVnqA2mHA53Rwn6fXzlF/vw+8juQJ2/K/hdN1/Ipx96hf54KrsLRHNNcNzbDZnCivl/IPffL+IbMU8saIwpYDKPPihFMI5V32LGrr53x3Xcet8zw8Lm2qUtfO+O69yNPeMpTvQO0hAeftkIB32c6B0kEvKzftUc1q+aw2AyzXPt3Wza03F26Dwx9oSAZNrhcE+UxnDAm6ruTjEPB3zZcFy/eg5fvOXyquhCmo6K/X8g8+9X7jiwY6TnsqAxpoBqOvqgGGPVt9ixq+/dcV3B5/f7hKaIO+vuRO8gNQEfjneGQizpMK9x+MLQSNDP+lVtrF/Vlg2dzXs6ebb9FPERWjMAcxuGxormN0Y4NRAnEvTjqOLgrg9qra+hqz9ObcjPulVtFixlUsr/B2wdjTEFLGqpZTA5fOuQaj4LZaz6jrbOZjzuuGEZacdtcQR9QiLtkHaUDVctGvExmdD53H+7iB/93nV87r9dxKULmgretykS4tEdx+kdTLLhqkWkHDdc1AuZlKN8aM0iegeTnDgTG1owGk1mF9Oa0ijl/wNi54ANt2bNGt2+fXulq2EqLLd/OrcFcC4X58kwmfXNDBDndlddt7yVvlgyO15SjKf3dPGNX+53Z6+lnWGHwPl9wpsXN7O4pZbdJ/roGogzrzHChqsWsTZnl4d8AZ+PcMjnHvY2Q/dlK5Xx/psSkRdUdU2h57KgyWNBYzIKXVCrMWQyqqG+qspAIk1fLMngODaTjCXTPLe/m8273e613MkCfp9wxaJmd/ba8tZxrTEK+n3Z00UjQX/2EDpTnPH8m7KgGQcLGmNKw90hIEV/LEXKKb5bK5ZMs22/O6aztf0UsZytE3wCb17szl67fsX4QkdEqAn4skdbh8uwuelMZkEzDhY0xpSWux9amt5xtnLAC50DbkunUOhc4YXOW5e30lQ7vt0U/N407XBo5h5/UEoWNONgQWNM+WRaOX2xZNFjORnxZJptB3rcls4bp4YNVPsErljUzLpVbVy/vHXMnQ4KyRx/EAn5CQesm228LGjGwYLGmPLLtHL6YqkxV5UXEk+mef5AD5tGCJ03LWp2Wzorzi108rvZSr0h6HRkQTMOFjTGTK5zHcvJyITO5j2dPFOG0HGfRwh7oRMJ+gmdy/ba05wFzThY0BhTGRNt5YB7MN3zB7rZtLtw6Fy+qJn13kSClnMMHRg+jbo2FBh2supMZUEzDhY0xlTeRFs5MBQ6mZZONHF26GRaOhMJHYBQ7my2GTq+Y0EzDhY0xlSPUrRyYHjobH3jFAN5oXPZwqHQmVU3sdDJjO/UelOoZ8o0aguacbCgMaY6laKVA27obD/YzeY9XTyzr6tA6DR5odM24dCBmTON2oJmHCxojKluE1mXky+RcnjhoDuR4Jd5oSO4obN+VelCB6bvbgUWNONgQWPM1JFIOfTGkvTHUu5u0hN8rmzovNHFQPzs0Fm3so0bVpYudKbTbgUzPmhE5Cbgy4Af+Jqq3j3SfS1ojJl6HEfpT6ToHSzNLs6JlMOLh3rYtLtw6FyaCZ0Vrcyur5nw62X4RNzWjtfiCU6hbrYZHTQi4gf2AL8OHAGeB25V1dcK3d+CxpipLZZ0u9UG4mlKcX3LhM7mPZ08vW/yQgemVjfbTA+aa4HPq+qN3vefAVDVvyl0fwsaY6YHx1H64u52N6U6qyaZzh3TOUV/fGgmnACXLMh0r7XSWuLQqfZutpkeNLcAN6nqx7zvPwxcraq/n3Of24HbARYvXnzlwYMHK1JXY0x5xFPp7Iy1iY7lZFQydMCdzZa7W0Glu9lmetB8ALgxL2jWqur/V+j+1qIxZvpSVfrjKfrjqQnPWMuVTHvda7u7+OUbXfTF8kOnMTtluq2h9KEDbjdbOOh3NwatQDfbaEETmNSaVMYRIPec2YXAsQrVxRhTQSJCQzhIQzhYsnU54F7kr146m6uXziaVXsGLh05nx3T6Yil2HO1lx9FevvKLN7jkvEbWrWrjhhKHTjLteD9Tsuq62WZCiyaAOxng7cBR3MkAv6WqOwvd31o0xswspdp9oJBU2uGlw6fZvNsNnd7Y8Oe/+Dy3pbNuZflaOjA5i0ZndNcZgIi8C/hH3OnN31DVvx7pvhY0xsxcqex5ORNv5RR67moIHRiazZbpZivFEQgzPmjGw4LGGFPK3QcKGSt0Lprvdq+tW9HKnMZwyV8/l4gQDuaevXNu3WwWNONgQWOMyZVIueMefSWcsZYrGzp7Onl6b6HQaWDdqjmTEjow1M2Wmc1WbDebBc04WNAYYwrJzFjrjaWIJ0vfygE3dF4+fJrNe7p4am9n4dDxtsGZOwmhA8OPQBitm82CZhwsaIwxY4mn0vQOphiIl6eVA5B21AudTp7a28WZweSw2y/MCZ15kxQ6mW622mCAcMg3rJvNgmYcLGiMMcUq9R5rI0k7yis5oXM6L3RWz3NDZ92qyQsdGH7SaGMkZEFTLAsaY8y5KPUeayNJO8orR9yJBIVCZ9W8BtZ7s9fmNU1e6Fwwp8GCplgWNMaYicjssdY7mCSZLl8rB3JCZ08nT+0pHDrrVraxfhJCx4JmHCxojDGlMlmtHBgeOk/v7aInmhc6cxvcKdMrW5nfFCn561vQjIMFjTGm1NKO0h9L0Rsrfysn83q/OjI0e61g6KxsZd2qtpKFjgXNOFjQGGPKaTJbOeCGzo6jZ9i0u7Ng6KycW5/dkeC85nMPHQuacbCgMcZMhrTjrcuZhLGc3Nd89egZNnmz17oHEsNuXzGnPjt7bcE4Q8eCZhwsaIwxky2WTNM7mGQgMTmtHPBC51impXN26CyfU5+dvbagZezQsaAZBwsaY0ylpB3NbnczWa2czOu+euwMm3d3suUcQ8eCZhwsaIwx1SCaSNE7WPqjC8aSdpSdOS2dU/mh01bP+lVnh44FzThY0Bhjqkkye3RBkrQzuddrR90xnc17utiyp7Ng6Kxb1eqN68y1oCmWBY0xphqpKgMJdywnVqZNPUczVugcvOc3ZvRRzsYYM+WJCPU1AeprAsRT6ewx1OXa1DOfT4TLFjZz2cJmPvFrF7DzaC+b93SyeW8np/oToz7WWjR5rEVjjJkqMpt69pXx6IIx66DKa8d6ee8VC61FY4wx043PJzSGgzSGgxVp5YDb0rlkQdOo97GgMcaYaaAm4Kem3s/suhD9cbeVU4mxnEIsaIwxZhoRERrCQRrCQRIpxwudyZ+xlsuCxhhjpqlQwMesQIiW2iDRhNu1NtnrcsCCxhhjpj0Roa4mQF1NgFTayXatTdbuAxY0xhgzgwT8PpprQzTXhhhMpOmLlX+PNQsaY4yZoSIhP5GQv+zn5VjQGGPMDOf3CU21QZpqg2Vp5VjQGGOMycq0cjJjOb2DKVLOxFo5FjTGGGPOkjuWM+BNHjjXGWu+EtetKCLyARHZKSKOiKzJu+0zIrJPRHaLyI055VeKyA7vtntFRLzyGhH5gVf+nIgsyXnMbSKy1/u4bdJ+QGOMmUbqagLMawqzaFYtTZEgfp+M6/EVCRrgVeD9wJbcQhG5CNgAXAzcBPyLiPi9m78K3A6s8D5u8so/CvSo6nLgS8A93nPNAj4HXA2sBT4nIi1l/JmMMWZaC/p9zK6vYfGsWtoaaqgJ+sd+EBUKGlV9XVV3F7jpvcD3VTWuqvuBfcBaEZkPNKrqVnVHp74NvC/nMd/yvn4IeLvX2rkReEJVu1W1B3iCoXAyxhhzjjK7DyxojrCgJUJDODjq/SvVohnJAuBwzvdHvLIF3tf55cMeo6op4Awwe5TnOouI3C4i20Vke2dnZwl+DGOMmRlqAn7aGmpGvU/ZJgOIyJPAvAI3/ZmqPjzSwwqU6Sjl5/qY4YWq9wP3g3tMwAh1M8YYcw7KFjSq+o5zeNgRYFHO9wuBY175wgLluY85IiIBoAno9srX5z1m0znUyRhjzARUW9fZI8AGbybZUtxB/22qehzoE5FrvPGXjwAP5zwmM6PsFmCjN47zOPBOEWnxJgG80yszxhgziSqyjkZE/jvwT0Ab8BMReVlVb1TVnSLyIPAakAI+oaqZAxU+DnwTiACPeh8AXwceEJF9uC2ZDQCq2i0ifwk8793vC6raXf6fzhhjTC47yjmPHeVsjDHjJyIjHuVcbV1nxhhjphkLGmOMMWVlQWOMMaasLGiMMcaUlU0GyCMincDBStcjRyvQVelKjIPVt7ysvuVl9T1356tqW6EbLGiqnIhsH2kmRzWy+paX1be8rL7lYV1nxhhjysqCxhhjTFlZ0FS/+ytdgXGy+paX1be8rL5lYGM0xhhjyspaNMYYY8rKgsYYY0xZWdBUCRFZJCK/EJHXRWSniHzKK58lIk+IyF7vc0ul6wqj1vfzInJURF72Pt5V6boCiEhYRLaJyCteff+vV16t7+9I9a3K9zdDRPwi8pKI/Jf3fVW+vxkF6lu176+IHBCRHV69tntlVf3+ZtgYTZUQkfnAfFV9UUQagBeA9wG/DXSr6t0ichfQoqp3Vq6mrlHq+0GgX1W/WMn65fPOMapT1X4RCQJPA58C3k91vr8j1fcmqvD9zRCR/wOsARpV9TdE5G+pwvc3o0B9P0+Vvr8icgBYo6pdOWVV/f5mWIumSqjqcVV90fu6D3gdWAC8F/iWd7dv4V7MK26U+lYldfV73wa9D6V639+R6lu1RGQh8G7gaznFVfn+woj1nWqq9v3NZUFThURkCXAF8Bww1zthFO/znApWraC8+gL8voj8SkS+UU1Nea+b5GWgA3hCVav6/R2hvlCl7y/wj8CfAE5OWdW+vxSuL1Tv+6vAz0TkBRG53Sur5vc3y4KmyohIPfBD4A9UtbfS9RlLgfp+FbgAeBNwHPj7ytVuOFVNq+qbgIXAWhG5pMJVGtUI9a3K91dEfgPoUNUXKl2XYoxS36p8fz1vUdU3AzcDnxCRGypdoWJZ0FQRry/+h8B/qOqPvOKT3nhIZlyko1L1y1eovqp60rtAOsC/AWsrWcdCVPU0sAl3vKNq39+M3PpW8fv7FuA93jjC94G3ich3qN73t2B9q/j9RVWPeZ87gB/j1q1a399hLGiqhDf4+3XgdVX9h5ybHgFu876+DXh4sutWyEj1zfyj9/x34NXJrlshItImIs3e1xHgHcAuqvf9LVjfan1/VfUzqrpQVZcAG4CNqvo/qdL3d6T6Vuv7KyJ13qQbRKQOeCdu3ary/c0XqHQFTNZbgA8DO7x+eYA/Be4GHhSRjwKHgA9UpnpnGam+t4rIm3D7kw8Ad1SicgXMB74lIn7cP7AeVNX/EpGtVOf7O1J9H6jS93ck1frvdyR/W6Xv71zgx+7fdwSA76rqYyLyPFPg/bXpzcYYY8rKus6MMcaUlQWNMcaYsrKgMcYYU1YWNMYYY8rKgsYYY0xZWdAYUyQRWSIiZ62rEJEviMg7xnjs50Xk0+WrnTHVy9bRGDNBqvrZStfBmGpmLRpjxscvIv8m7hkxPxORiIh8U0RuARCRd4nILhF5WkTuzZxz4rlIRDaJSLuIfNK7/5/kfP0lEdnoff12bwsXROSrIrJdhp9L83YR+XHmiUXk10XkR+TxWlLf8up6QETeLyJ/K+65Jo952whlzjq5R9wzcLaJyHKv/AIReVZEnvdabv35r2HMWCxojBmfFcA/q+rFwGngNzM3iEgYuA+4WVWvB9ryHrsauBF3j6rPeRf5LcBbvdvXAPVe+fXAU175n6nqGuAyYJ2IXAZsBC4Ukcxr/C/g30eo8wW42+G/F/gO8AtVvRQY9MozelV1LfAV3J2NAb4MfFlVrwKOjf7WGFOYBY0x47NfVV/2vn4BWJJz22qgXVX3e99/L++xP1HVuHdwVQfutiIvAFd6+1jFga24gfNWhoLmgyLyIvAScDFwkbpbejwA/E9vT7RrgUdHqPOjqpoEdgB+4DGvfEde/b+X8/la7+trgf/0vv7uCM9vzKhsjMaY8YnnfJ0GIjnfyzgfG1DVpLeD8P8CngF+BfwabivkdRFZCnwauEpVe0Tkm0DYe45/B/4fEAP+U1VTIvIJ4He92zPHEMcBVNURkaQO7TvlMPwaoCN8bcyEWIvGmNLZBSwT9yA4gA8V+bgtuGGyBbcV87+Bl71AaAQGgDMiMhf3LBIgu238MeDPgW96Zf+sqm/yPsbb1fWhnM9bva+fZah7cMM4n88YwFo0xpSMqg6KyO8Bj4lIF7CtyIc+BfwZsFVVB0Qk5pWhqq+IyEvATqAd+GXeY/8DaFPV10rwI9SIyHO4f4De6pX9AfAdEfkj4CfAmRK8jplhbPdmY0pIROpVtd87r+efgb2q+qUyvt5XgJdU9esTfJ4DwBpv/Ci3vBYYVFUVkQ3Arar63om8lpl5rEVjTGn9rojcBoRwB+/vK9cLicgLuN1qf1Su1wCuBL7iBedp4HfK+FpmmrIWjTHGmLKyyQDGGGPKyoLGGGNMWVnQGGOMKSsLGmOMMWVlQWOMMaas/n92lzizJ20x5QAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# vamos observar agora a coluna 'highway-mpg' e 'price'\n",
    "sns.regplot(x='highway-mpg', y='price', data=df)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "c764ba06-7645-4eea-8fa8-ab0876c2e3a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>highway-mpg</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>highway-mpg</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.704692</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>price</th>\n",
       "      <td>-0.704692</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             highway-mpg     price\n",
       "highway-mpg     1.000000 -0.704692\n",
       "price          -0.704692  1.000000"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['highway-mpg','price']].corr()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d29e1186-78ac-4f56-b20f-0ca0c0efcab3",
   "metadata": {},
   "source": [
    "A medida que 'highway-mpg' aumenta o preço diminui indicando uma relação inversa/negativa entre essas duas variáveis.\n",
    "highway-mpg pode ser também um preditor para o preço\n",
    "> A correlação entre essas variáveis é de aproximadamente -0.70. oque mostra ser uma correlação negativa mas boa para prever o preço "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "679d2182-90b6-473e-96a1-92906209b5f0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# analisando 'stroke'\n",
    "sns.regplot(x='stroke', y='price', data=df)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "735c102e-7602-4ef3-92c4-862673c15414",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>stroke</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>stroke</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.082267</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>price</th>\n",
       "      <td>0.082267</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          stroke     price\n",
       "stroke  1.000000  0.082267\n",
       "price   0.082267  1.000000"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['stroke','price']].corr()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7930ff98-ca3e-447d-95c8-a2598b055471",
   "metadata": {},
   "source": [
    "Entre a variável stroke e preço existe o correlação fraca. podemos obersvar que a regresão não funciona legal, ja que os dados estão espalhados e não apresenta uma linearidade\n",
    "> Correlação aproximada de 0.08 , muito fraca"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "059f64d6-7d2a-495c-8e34-73c0a9a455de",
   "metadata": {},
   "source": [
    "### Variáveis Categóricas "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "70475fc1-41c0-40cc-91fc-44086612de45",
   "metadata": {},
   "source": [
    "verificando o relacionamento entre 'body-style' and 'price'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "c9144268-ce40-470d-9410-7b6dcd4db24d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# gerando um boxplot entre 'body-style' e 'price'\n",
    "sns.boxplot(x='body-style', y='price', data=df)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "703744e5-08af-4e88-a0ec-87450541ff57",
   "metadata": {},
   "source": [
    "Na distribuição acima entre diferentes categorias de estilo do carro, notamos uma sobreposição significativa. indicando que talvez não seria uma boa preditora para o preço"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "fb1b728d-3ba2-4303-b14c-22af3d6f92b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# gerando um boxplot entre 'engine-location' e 'price'\n",
    "sns.boxplot(x='engine-location', y='price', data=df)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fab9747a-48ff-4969-ab0f-55584d850fbd",
   "metadata": {},
   "source": [
    "Na distribuição de preço entre essas duas categorias de localização do motor, vemos uma distinção entre dianteira e traseira. visto isso imaginamos 'engine-location' como uma potencial preditora para o preço"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "408932e6-f470-4b06-928d-46f3c4fec494",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# drive-wheels\n",
    "sns.boxplot(x='drive-wheels', y='price', data=df)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f4318277-d744-4798-a85b-52da75410cd4",
   "metadata": {},
   "source": [
    "Rodas motrizes também parece ser uma boa preditora de preço, já que sua distribuição de preço difere "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "31c85ce4-ec41-4d85-8ceb-e231d0fbd72d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>value_counts</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>drive-wheels</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>fwd</th>\n",
       "      <td>118</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>rwd</th>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4wd</th>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              value_counts\n",
       "drive-wheels              \n",
       "fwd                    118\n",
       "rwd                     75\n",
       "4wd                      8"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "drive_counts = df['drive-wheels'].value_counts().to_frame()\n",
    "drive_counts.rename(columns={'drive-wheels':'value_counts'},inplace=True)\n",
    "drive_counts.index.name = 'drive-wheels'\n",
    "drive_counts.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "2bd14c08-adb9-417a-a30c-801ec0fb7f47",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>value_counts</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>engine-location</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>front</th>\n",
       "      <td>198</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>rear</th>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 value_counts\n",
       "engine-location              \n",
       "front                     198\n",
       "rear                        3"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "engine_loc = df['engine-location'].value_counts().to_frame()\n",
    "engine_loc.rename(columns={'engine-location':'value_counts'},inplace=True)\n",
    "engine_loc.index.name = 'engine-location'\n",
    "engine_loc.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a7a29de7-05ef-47b9-a68f-e5f1fbf1398a",
   "metadata": {},
   "source": [
    "Como vemos em 'engine-location' apenas 3 carros no nosso conjunto de dados tem o motor na parte traseira oque da um resultado distorcido. então podemos concluir que esta variável não é uma boa preditora"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "e07fb3e5-3773-4656-8175-41c5d350ef15",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>drive-wheels</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>4wd</td>\n",
       "      <td>10241.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>fwd</td>\n",
       "      <td>9244.779661</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>rwd</td>\n",
       "      <td>19757.613333</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  drive-wheels         price\n",
       "0          4wd  10241.000000\n",
       "1          fwd   9244.779661\n",
       "2          rwd  19757.613333"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# agrupando por drive-wheels e obtendo a média de preço\n",
    "group_1 = df[['drive-wheels','body-style','price']]\n",
    "group_1 = group_1.groupby(['drive-wheels'], as_index=False).mean()\n",
    "group_1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "059b4ce0-ce55-4c6d-bafc-8f59e10db6f8",
   "metadata": {},
   "source": [
    "Podemos ver que em média os carros com tração traseira são mais caros, e os carros com tração nas 4 rodas e na frente tem uma similaridade nos preços"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "c07c78fb-e5d9-4461-8ec7-ebe8163a2168",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>drive-wheels</th>\n",
       "      <th>body-style</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>4wd</td>\n",
       "      <td>hatchback</td>\n",
       "      <td>7603.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4wd</td>\n",
       "      <td>sedan</td>\n",
       "      <td>12647.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4wd</td>\n",
       "      <td>wagon</td>\n",
       "      <td>9095.750000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>fwd</td>\n",
       "      <td>convertible</td>\n",
       "      <td>11595.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>fwd</td>\n",
       "      <td>hardtop</td>\n",
       "      <td>8249.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>fwd</td>\n",
       "      <td>hatchback</td>\n",
       "      <td>8396.387755</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>fwd</td>\n",
       "      <td>sedan</td>\n",
       "      <td>9811.800000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>fwd</td>\n",
       "      <td>wagon</td>\n",
       "      <td>9997.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>rwd</td>\n",
       "      <td>convertible</td>\n",
       "      <td>23949.600000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>rwd</td>\n",
       "      <td>hardtop</td>\n",
       "      <td>24202.714286</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>rwd</td>\n",
       "      <td>hatchback</td>\n",
       "      <td>14337.777778</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>rwd</td>\n",
       "      <td>sedan</td>\n",
       "      <td>21711.833333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>rwd</td>\n",
       "      <td>wagon</td>\n",
       "      <td>16994.222222</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   drive-wheels   body-style         price\n",
       "0           4wd    hatchback   7603.000000\n",
       "1           4wd        sedan  12647.333333\n",
       "2           4wd        wagon   9095.750000\n",
       "3           fwd  convertible  11595.000000\n",
       "4           fwd      hardtop   8249.000000\n",
       "5           fwd    hatchback   8396.387755\n",
       "6           fwd        sedan   9811.800000\n",
       "7           fwd        wagon   9997.333333\n",
       "8           rwd  convertible  23949.600000\n",
       "9           rwd      hardtop  24202.714286\n",
       "10          rwd    hatchback  14337.777778\n",
       "11          rwd        sedan  21711.833333\n",
       "12          rwd        wagon  16994.222222"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# agrupando por 'drive-wheels' e 'body-style' e obtendo a média de preço para cada tipo\n",
    "gp_test = df[['drive-wheels','body-style','price']]\n",
    "group_1_test = gp_test.groupby(['drive-wheels','body-style'], as_index=False).mean()\n",
    "group_1_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "a6c113d3-e3a2-41ff-925f-456bdf06c692",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr:last-of-type th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr>\n",
       "      <th></th>\n",
       "      <th colspan=\"5\" halign=\"left\">price</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>body-style</th>\n",
       "      <th>convertible</th>\n",
       "      <th>hardtop</th>\n",
       "      <th>hatchback</th>\n",
       "      <th>sedan</th>\n",
       "      <th>wagon</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>drive-wheels</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4wd</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>7603.000000</td>\n",
       "      <td>12647.333333</td>\n",
       "      <td>9095.750000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>fwd</th>\n",
       "      <td>11595.0</td>\n",
       "      <td>8249.000000</td>\n",
       "      <td>8396.387755</td>\n",
       "      <td>9811.800000</td>\n",
       "      <td>9997.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>rwd</th>\n",
       "      <td>23949.6</td>\n",
       "      <td>24202.714286</td>\n",
       "      <td>14337.777778</td>\n",
       "      <td>21711.833333</td>\n",
       "      <td>16994.222222</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   price                                            \\\n",
       "body-style   convertible       hardtop     hatchback         sedan   \n",
       "drive-wheels                                                         \n",
       "4wd                  NaN           NaN   7603.000000  12647.333333   \n",
       "fwd              11595.0   8249.000000   8396.387755   9811.800000   \n",
       "rwd              23949.6  24202.714286  14337.777778  21711.833333   \n",
       "\n",
       "                            \n",
       "body-style           wagon  \n",
       "drive-wheels                \n",
       "4wd            9095.750000  \n",
       "fwd            9997.333333  \n",
       "rwd           16994.222222  "
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# fazendo um pivot do dataframe obtido, que é basicamente inverter as colunas com as linhas tornando melhor a análise e visualização\n",
    "grouped_pivot = group_1_test.pivot(index='drive-wheels', columns='body-style')\n",
    "grouped_pivot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "902ab475-c501-410a-835a-7971ed49a4ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr:last-of-type th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr>\n",
       "      <th></th>\n",
       "      <th colspan=\"5\" halign=\"left\">price</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>body-style</th>\n",
       "      <th>convertible</th>\n",
       "      <th>hardtop</th>\n",
       "      <th>hatchback</th>\n",
       "      <th>sedan</th>\n",
       "      <th>wagon</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>drive-wheels</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4wd</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7603.000000</td>\n",
       "      <td>12647.333333</td>\n",
       "      <td>9095.750000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>fwd</th>\n",
       "      <td>11595.0</td>\n",
       "      <td>8249.000000</td>\n",
       "      <td>8396.387755</td>\n",
       "      <td>9811.800000</td>\n",
       "      <td>9997.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>rwd</th>\n",
       "      <td>23949.6</td>\n",
       "      <td>24202.714286</td>\n",
       "      <td>14337.777778</td>\n",
       "      <td>21711.833333</td>\n",
       "      <td>16994.222222</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   price                                            \\\n",
       "body-style   convertible       hardtop     hatchback         sedan   \n",
       "drive-wheels                                                         \n",
       "4wd                  0.0      0.000000   7603.000000  12647.333333   \n",
       "fwd              11595.0   8249.000000   8396.387755   9811.800000   \n",
       "rwd              23949.6  24202.714286  14337.777778  21711.833333   \n",
       "\n",
       "                            \n",
       "body-style           wagon  \n",
       "drive-wheels                \n",
       "4wd            9095.750000  \n",
       "fwd            9997.333333  \n",
       "rwd           16994.222222  "
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grouped_pivot = grouped_pivot.fillna(0) # prenche os valores missing com 0\n",
    "grouped_pivot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "7a7ccc54-1cba-4575-852f-9d904d5deee4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>body-style</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>hardtop</td>\n",
       "      <td>22208.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>convertible</td>\n",
       "      <td>21890.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>sedan</td>\n",
       "      <td>14459.755319</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>wagon</td>\n",
       "      <td>12371.960000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>hatchback</td>\n",
       "      <td>9957.441176</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    body-style         price\n",
       "1      hardtop  22208.500000\n",
       "0  convertible  21890.500000\n",
       "3        sedan  14459.755319\n",
       "4        wagon  12371.960000\n",
       "2    hatchback   9957.441176"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# agrupamento de 'body-style' e obtendo a média de preço\n",
    "body_group = df[['body-style', 'price']]\n",
    "body_group = body_group.groupby(['body-style'], as_index=False).mean()\n",
    "# usando metodo sort_values para ordenar os preços do maior para o menor\n",
    "body_asce = body_group.sort_values(by='price' , axis=0, ascending=False)\n",
    "body_asce"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "6637eb14-8550-4d1f-b2a0-f9de016a140a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax =plt.subplots()\n",
    "im = ax.pcolor(grouped_pivot, cmap = 'RdYlBu')\n",
    "\n",
    "# nome dos labels\n",
    "row_labels = grouped_pivot.columns.levels[1]\n",
    "col_labels = grouped_pivot.index\n",
    "\n",
    "# movendo marcas e labels para o centro\n",
    "ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)\n",
    "ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)\n",
    "\n",
    "# inserindo labels\n",
    "ax.set_xticklabels(row_labels, minor=False)\n",
    "ax.set_yticklabels(col_labels, minor=False)\n",
    "\n",
    "# rotacionando\n",
    "plt.xticks(rotation=15)\n",
    "\n",
    "fig.colorbar(im)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb69d583-725b-4606-bd91-e60d66f50e6a",
   "metadata": {},
   "source": [
    "---\n",
    "Quais são as variáveis que mais impactam no preço do carro?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "64fdbb7b-698a-4811-8644-51018f4df4e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy import stats"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f7f604ab-d157-4cbb-855c-309c93c06bd2",
   "metadata": {},
   "source": [
    "### P-value"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f5d31067-ebaa-4e25-a30f-dbd6fa9bbec4",
   "metadata": {},
   "source": [
    "O valor de P é o valor da probabilidade de que a correlação entre essas duas variáveis seja estatisticamente significativa. Normalmente escolhemos o valor de P como 0.05, oque significa que temos 95% de confiança de que a correlação entre as variáveis é significativa"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "6cfd54c9-24b3-4b40-aa13-708eae6ab86b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coeficiente de correlação de pearson é 0.584641822265508 com o P-value de 8.076488270733218e-20\n"
     ]
    }
   ],
   "source": [
    "# correlação entre 'wheel-base' e 'price'\n",
    "pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])\n",
    "print('Coeficiente de correlação de pearson é {} com o P-value de {}' .format(pearson_coef, p_value))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3b7c5f2-0d05-4557-a87e-94e2028dc733",
   "metadata": {},
   "source": [
    "> Conclusão: \n",
    "O valor de P é < 0.001, correlação estatisticamente significativa, embora a relação linear não seja muito forte(~ 0.584)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "ea94ef71-952c-4bde-829d-58f83c44dee5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coeficiente de correlação de pearson é 0.8097290352560285 com o P-value de 5.924001027593172e-48\n"
     ]
    }
   ],
   "source": [
    "# correlação entre 'horsepower' e 'price'\n",
    "pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])\n",
    "print('Coeficiente de correlação de pearson é {} com o P-value de {}' .format(pearson_coef, p_value))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c909c147-37f2-4d23-b276-681d36b62b89",
   "metadata": {},
   "source": [
    "> Conclusão: O valor de P é < 0.001, correlação estatisticamente significativa, e uma relação linear forte (~ 0.809)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "b031416e-9f52-4f1a-9207-1eea4ff41311",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coeficiente de correlação de pearson é 0.6906283804483639 com o P-value de 8.016477466159328e-30\n"
     ]
    }
   ],
   "source": [
    "# correlação entre 'length' e 'price'\n",
    "pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])\n",
    "print('Coeficiente de correlação de pearson é {} com o P-value de {}' .format(pearson_coef, p_value))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "70c80180-747f-400e-bb22-965b7c442ee7",
   "metadata": {},
   "source": [
    "> Conclusão: O valor de P é < 0.001, correlação estatisticamente significativa, com uma relação linear moderadamente forte (~ 0.690)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "456ee30c-e477-4e24-ae38-6b69d6448afc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coeficiente de correlação de pearson é 0.7512653440522673 com o P-value de 9.200335510481646e-38\n"
     ]
    }
   ],
   "source": [
    "# correlação entre 'width' e 'price'\n",
    "pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])\n",
    "print('Coeficiente de correlação de pearson é {} com o P-value de {}' .format(pearson_coef, p_value))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0d9953d7-7cb7-447a-8418-c0cf3e37eb2c",
   "metadata": {},
   "source": [
    "> Conclusão: O valor de P é < 0.001, correlação estatisticamente significativa, e uma relação linear bastante forte (~ 0.751)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "c452e455-af79-436b-a05f-baf1ad773759",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coeficiente de correlação de pearson é 0.8344145257702843 com o P-value de 2.189577238894065e-53\n"
     ]
    }
   ],
   "source": [
    "# curb-weight\n",
    "pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])\n",
    "print('Coeficiente de correlação de pearson é {} com o P-value de {}' .format(pearson_coef, p_value))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47f5bf8b-b50e-43d4-9036-19d25e9b3024",
   "metadata": {},
   "source": [
    "> Conclusão: O valor de P é < 0.001, correlação estatisticamente significativa, e uma relação linear bastante forte (~ 0.834)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "a177af85-e48b-470e-9da4-ec0a64afe6c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coeficiente de correlação de pearson é 0.8723351674455185 com o P-value de 9.265491622198389e-64\n"
     ]
    }
   ],
   "source": [
    "# engine-size\n",
    "pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])\n",
    "print('Coeficiente de correlação de pearson é {} com o P-value de {}' .format(pearson_coef, p_value))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d35e515-a3c9-482f-8b5c-08b0792bf81b",
   "metadata": {},
   "source": [
    "> Conclusão: O valor de P é < 0.001, correlação estatisticamente significativa, e uma relação linear bastante forte (~ 0.872)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "f3d8aa93-abf5-4bac-bbcb-e83a35fc9e45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coeficiente de correlação de pearson é 0.5431537659807734 com o P-value de 8.051208825441016e-17\n"
     ]
    }
   ],
   "source": [
    "# 'bore'\n",
    "pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])\n",
    "print('Coeficiente de correlação de pearson é {} com o P-value de {}' .format(pearson_coef, p_value))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c0f8792-030f-4c0d-86e2-fe6e997b7134",
   "metadata": {},
   "source": [
    "> Conclusão: O valor de P é < 0.001, correlação estatisticamente significativa, e uma relação linear moderada (~ 0.543) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "ab3a26e5-3c27-4a36-8984-c4268974037a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coeficiente de correlação de pearson é -0.6865710067844677 com o P-value de 2.321132065567674e-29\n"
     ]
    }
   ],
   "source": [
    "# 'city-mpg'\n",
    "pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])\n",
    "print('Coeficiente de correlação de pearson é {} com o P-value de {}' .format(pearson_coef, p_value))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "49d71b4d-2e9b-470c-9a60-63c060b6f4c7",
   "metadata": {},
   "source": [
    "> Conclusão: O valor de P é < 0.001, correlação estatisticamente significativa, e uma relação linear negativa e moderadamente forte com aproximadamente - 0.686"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "9148d0a8-eb2b-4db5-8cb8-0b1ac12be1cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coeficiente de correlação de pearson é -0.704692265058953 com o P-value de 1.7495471144476358e-31\n"
     ]
    }
   ],
   "source": [
    "# 'highway-mpg'\n",
    "pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])\n",
    "print('Coeficiente de correlação de pearson é {} com o P-value de {}' .format(pearson_coef, p_value))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5bd4ced4-48c7-4f85-9f43-c8e977c61254",
   "metadata": {},
   "source": [
    "> Conclusão: O valor de P é < 0.001, correlação estatisticamente significativa, e uma relação linear negativa e moderadamente forte com aproximadamente - 0.704"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f3c8e0a3-e7c4-4909-99c3-5c73a66b8953",
   "metadata": {},
   "source": [
    "### ANOVA"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "86857386-d539-49ce-b18a-c68af45d2f1f",
   "metadata": {},
   "source": [
    "---\n",
    "A Análise de Variância (ANOVA) é um método estatístico utilizado para testar se existem diferenças significativas entre as médias de dois ou mais grupos. ANOVA retorna dois parâmetros:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "777b042e-ad71-4f0d-8d69-4cb0e46c68ac",
   "metadata": {},
   "source": [
    "> **Pontuação do teste F**: ANOVA assume que as médias de todos os grupos são as mesmas, calcula o quanto as médias reais se desviam da suposição e informa como a pontuação do teste F. Uma pontuação maior significa que há uma diferença maior entre as médias.\n",
    "\n",
    ">**Valor-P**: o valor-P informa o quão estatisticamente significativo é o nosso valor de pontuação calculado.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "3830ba81-f2f4-4c04-9b0b-35b6885945e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>drive-wheels</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>rwd</td>\n",
       "      <td>13495.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>rwd</td>\n",
       "      <td>16500.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>fwd</td>\n",
       "      <td>13950.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4wd</td>\n",
       "      <td>17450.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>fwd</td>\n",
       "      <td>15250.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>140</th>\n",
       "      <td>4wd</td>\n",
       "      <td>7603.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    drive-wheels    price\n",
       "0            rwd  13495.0\n",
       "1            rwd  16500.0\n",
       "3            fwd  13950.0\n",
       "4            4wd  17450.0\n",
       "5            fwd  15250.0\n",
       "140          4wd   7603.0"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grouped_test2 = gp_test[['drive-wheels', 'price']].groupby(['drive-wheels'])\n",
    "grouped_test2.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "a6abbb3d-5bc9-4c12-b69d-2f11fb79c726",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>drive-wheels</th>\n",
       "      <th>body-style</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>rwd</td>\n",
       "      <td>convertible</td>\n",
       "      <td>13495.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>rwd</td>\n",
       "      <td>convertible</td>\n",
       "      <td>16500.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>rwd</td>\n",
       "      <td>hatchback</td>\n",
       "      <td>16500.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>fwd</td>\n",
       "      <td>sedan</td>\n",
       "      <td>13950.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  drive-wheels   body-style    price\n",
       "0          rwd  convertible  13495.0\n",
       "1          rwd  convertible  16500.0\n",
       "2          rwd    hatchback  16500.0\n",
       "3          fwd        sedan  13950.0"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gp_test.head(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "3f525950-40e9-414a-bbaf-47ddb339873a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4      17450.0\n",
       "140     7603.0\n",
       "144     9233.0\n",
       "145    11259.0\n",
       "148     8013.0\n",
       "149    11694.0\n",
       "154     7898.0\n",
       "155     8778.0\n",
       "Name: price, dtype: float64"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grouped_test2.get_group('4wd')['price']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "5750c29e-82b2-4353-8875-32cb2731abb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ANOVA results: F= 67.95406500780399 , P = 3.3945443577151245e-23\n"
     ]
    }
   ],
   "source": [
    "f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'], grouped_test2.get_group('4wd')['price'])  \n",
    " \n",
    "print( \"ANOVA results: F=\", f_val, \", P =\", p_val)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "53f8118e-a521-47d0-a371-d747938896dc",
   "metadata": {},
   "source": [
    "Este é um ótimo resultado com uma grande pontuação no teste F mostrando uma forte correlação e um valor P de quase 0 implicando uma significância estatística quase certa. Mas isso significa que todos os três grupos são altamente correlacionados?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "da191658-d764-4103-8d01-7960d1e89d77",
   "metadata": {},
   "source": [
    "* fwd and rwd¶"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "bd385d02-087e-44b3-bc46-c4404780a55c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ANOVA results: F= 130.5533160959111 , P = 2.2355306355677845e-23\n"
     ]
    }
   ],
   "source": [
    "f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'])  \n",
    " \n",
    "print( \"ANOVA results: F=\", f_val, \", P =\", p_val )"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "22bf033e-0b48-467c-a018-6e73cd6b5ab4",
   "metadata": {},
   "source": [
    "* 4wd and rwd¶"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "5583ba06-da7d-491e-8104-286e37a06599",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ANOVA results: F= 8.580681368924756 , P = 0.004411492211225333\n"
     ]
    }
   ],
   "source": [
    "f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('rwd')['price'])  \n",
    "   \n",
    "print( \"ANOVA results: F=\", f_val, \", P =\", p_val)   "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5b99086-80c6-45da-813b-b340c29189d1",
   "metadata": {},
   "source": [
    "* 4wd and fwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "e2285253-71e7-4b54-b310-371f551340d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ANOVA results: F= 0.665465750252303 , P = 0.41620116697845666\n"
     ]
    }
   ],
   "source": [
    "f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('fwd')['price'])  \n",
    " \n",
    "print(\"ANOVA results: F=\", f_val, \", P =\", p_val) "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5042c627-2945-4f66-a429-c3400b808894",
   "metadata": {},
   "source": [
    "## Conclusão: Variáveis Importantes\n",
    "Agora temos uma ideia melhor de como são nossos dados e quais variáveis são importantes a serem levadas em consideração ao prever o preço do carro. Reduzimos para as seguintes variáveis:\n",
    "> Variáveis Númericas\n",
    "* Length\n",
    "* Width\n",
    "* Curb-weight\n",
    "* Engine-size\n",
    "* Horsepower\n",
    "* City-mpg\n",
    "* Highway-mpg\n",
    "* Wheel-base\n",
    "* Bore"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "334c6da8-3ac8-44e0-ae3b-e65c4d7854e1",
   "metadata": {},
   "source": [
    "> Variáveis Categoricas\n",
    "* Drive-wheels"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "38f96482-0b7d-4286-9f84-000a0f55d9ee",
   "metadata": {},
   "source": [
    "Desenvolvimento de modelo\n",
    "---\n",
    "Faremos agora alguns modelos de regressão para prever o preço dos carros "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c457a5bd-3736-4f95-8afe-91171b342acd",
   "metadata": {},
   "source": [
    "### Regressão linear simples"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "9ea5a2a2-fb15-4fbe-83d5-f4867439c6c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# importando a regressão linear a partir da biblioteca sklearn\n",
    "from sklearn.model_selection import train_test_split \n",
    "from sklearn.linear_model import LinearRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "01563b53-2df3-4fb9-9c6a-c665b55f1b10",
   "metadata": {},
   "outputs": [],
   "source": [
    "# definindo a variável dependente e independente\n",
    "y = df['price']\n",
    "x = df.drop('price', axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "10625049-a495-48bc-9bb6-33d0f73412b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Amostra teste: 61\n",
      "Amostra treino: 140\n"
     ]
    }
   ],
   "source": [
    "# dividindo o conjunto de dados entre amostra de treino e de teste\n",
    "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=1)\n",
    "\n",
    "print('Amostra teste: {}'.format(x_test.shape[0]))\n",
    "print('Amostra treino: {}'.format(x_train.shape[0]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "516e545e-d904-4af4-854d-f234b0be36d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# atribuindo a função linear regression a variável lm e fitando o modelo com as variáveis dependente e independente\n",
    "lm = LinearRegression()\n",
    "lm.fit(x_train[['horsepower']], y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "babfa333-e619-4372-b4fd-6b55c891f753",
   "metadata": {},
   "outputs": [],
   "source": [
    "# usando o método predict para prever os preços a partir de x\n",
    "yhat = lm.predict(x_test[['horsepower']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "22fb82c9-1fca-4b64-b8d4-f719ee9b89f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([12123.93271467,  7107.6490916 ,  9875.25384916,  8491.45147038,\n",
       "       15410.46336427])"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "yhat[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "495c5f9e-f4e1-4c12-9419-08f981336cb0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.629225028951067"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# usando a metrica de R^2  \n",
    "lm.score(x_test[['horsepower']], y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "56c9f356-c133-4357-b9c1-0756d3c2acea",
   "metadata": {},
   "source": [
    "> Podemos dizer que essa metrica acima estima que ~ 0.629% da variação do preço é esplicada por esse modelo linear simples"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "00e80891-25d3-47e1-af60-8cc7e5405326",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MSE: 4289.919369102071\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import mean_squared_error\n",
    "mse = mean_squared_error(y_test,yhat)\n",
    "print('MSE: {}'.format(np.sqrt(mse)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "e62aaf83-21d1-4312-97ae-5820218470da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-194214556.73703635"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(y_test - yhat**2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "915589c8-fe99-44ec-bc36-be8a0f1dd3d1",
   "metadata": {},
   "source": [
    ">Podemos dizer que o valor de MSE é oque o modelo ta perdendo "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "48c34654-6285-41a7-8f9b-4cef08d75bf6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MSLE: 0.28027383237867226\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import mean_squared_log_error\n",
    "msle = mean_squared_log_error(y_test, yhat)\n",
    "print('MSLE: {}'.format(np.sqrt(msle)))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eadf3721-6280-4c95-a379-6824b6f3a5b9",
   "metadata": {},
   "source": [
    "> O MSLE leva em consideração a diferença relativa entre a variável de entrada e o previsto"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "a57142d3-85b8-419e-9ffe-628f8ae9e419",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE: 3116.9242889066118\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import mean_absolute_error\n",
    "mae = mean_absolute_error(y_test, yhat)\n",
    "print('MAE: {}'.format(mae))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ffd062d4-4a4e-4b2a-954c-7683bdeddd42",
   "metadata": {},
   "source": [
    "> MAE usa como minimizador a mediana sendo assim menos afetado por outiliers e  comparando com o MSE, observamos que as duas métricas tem os valores próximos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "561b4fde-4899-47e8-bc59-58cb82fbd60a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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z39C3bo8+aTNP7vsMvsNbt48yvV79sDixXbCV1/BmjVWVrGihUkdc4zNTm7TJmxdRscpXxIm8CIiwHPAMlV9LFH3SQei+t9nzLC99+CTR8WK8OyztvL5vfdarOTNN1P9/PN5683DOb6TcMEFMGXCHip/9ZmNlM+eba61uXPtxwFMwA86CKpWhd27bdbU7t127PDDLWXxtddC48bJa6uTlYgmaPUDETkJmAYsAkIpne5W1Y8Ku6ZTp046J5iEkklccAF88omlnMnvzF1wAUyfboVO8pk3z/IWjBljf9esydZq9dmx4WfqVthMxbxg1LVqVeuZd+liT1+dOkGLFlClyr66du+GlSth2jTLbDZ5sh2/7jq46y6LxXecOCEic1W1U9RjiRL40pCJAq9qHbdeveDll8MKmzaF006DV15Jqn1OBF9+CePHm/tl40amzKvFx4vr0O+mI+k45DhzuYSLeSx88YXF3//nP9CggY3knnNOYux3so6iBN7DNxLMp59auPV+E5y++w5OPjlpdjmF0LKl5a0J6LoTbusOj74I826CliXUdsBcQMOH20zaIUPg3HNtZtXTT1uYrOMkCE9VkGDGj7d9Tk5Y4bRptneBT3mqVjUvi6otErJzZxkqO+YYc8vdf789uZ10EqxeHTdbHScSF/gEM3asdQpbtQornDYN6te3xDROyhPqgM+ZY53wMlG5sg3ofvABfP65+fDnz4+HmY6zHy7wCWT3bpg0Cfr0iTgwbZr13ir4258uDBpk2Q3+8Q+b8Vpm+ve33nzVqjYWM316HCp1nIK4wiSQmTNtRnwBgf/+e4uwcPdM2vHwwxY4c+WVNoxSZtq0sR/7Ro2gd+99+aQdJ064wCeQceOsk96zZ1hhaPkgF/i0o0oVeP11C3W98EKbjFxmDj3UhL15cxg4MD9XvePEAxf4BDJ6tPX46tYNK5w2zSInfJHttKRlS8tVNns23HlnnCpt3NhG4xs0gL59beqz48QBF/gEsXaticCAAREHJkyA7t1tsM1JS84+G66/3vKVvfdenCpt2tQe+SpXNpH3nMVOHHCBTxCjRlloXQGB/+YbWLIkyqirk248+qg9hA0ZEsfJyK1bw0cf2SIwZ54J27bFqWInW3GBTxAffghNmtiScPmMG2f73r2TYZITR6pWhTfesPxiF164L/VMmenQwVabmjMHLr88P1+945QGF/gEsGuXpTQZMCAikeC4cZaU6thjk2abEz9at7ZcZdOnw+9/H8eKzzwT/vxni8e89944VuxkGy7wCWDqVAuPLOCeycszge/d2+PfM4gLLrDU8o88Euf88bfdti8x/ZtvxrFiJ5twpUkAI0daoEwBT0xurqWRdfdMxvG3v8Fxx9liId98E6dKRSw/fbduJvTLlsWpYiebcIGPM3l58M470K9fRB4p979nLNWrWyd7+3ZbtDtu67lWqWIVV69u2Sd//jlOFTvZggt8nJk+3Sar7pcNduxYSzbliz5kJEceCf/+t7nnHnggjhU3awavvQYrVliWyxRK7+2kPi7wcWbkSOt4FfC/b95sE5w8PDKjufRS+OUv4Y9/tElucSMnxyp9/XVLhuM4MeICH0fy8uCtt0zHa9cOOzBqlIXWnHVW0mxzyod//MP88RddBJ99FseKf/tb+MUv4NZbPTGZEzMu8HFk2jRL733xxREHRo6EAw+0ATMnozngABuDqVDBfs/j5javUAFefBEOOcQS02/YEKeKnUzGBT6OvPoq1KgBZ5wRVrhjh81OPPNMW+TZyXhatjRvytKl5rKJm9u8Xj17RFy3zidBOTGRMIEXkedFZJ2ILE7UPVKJXbvsuzdokIl8PuPHWzfu7LOTZZqTBHr3tvTCI0bYnKW40bGjxWV+9JHlS3CcIkhkD3440DeB9acUH34IP/0El1wSceCdd8whXyBnsJMN3H67TYS66y6b2Rw3rr0WzjsP7r57X/ppx4lCwgReVacCPyaq/lRj2DDLPVMgzH3PHks3OHCghdY4WYUIPPecZaa44ALLMxe3iocNgxYtLBGO++OdQki6D15EhorIHBGZs379+mSbUypWr7awuF/+EipVCjswebJ9+Tx6JmupUQPef98GX/v1g2+/jVPFtWubT3D9eptC6/54JwpJF3hVfUZVO6lqp0aNGiXbnFLxwgv2/bryyogDw4dDnTpRksI72cQhh5gL78cf7WEubpE1HTrA449bGO5f/hKnSp1MIukCn+7s2WNPy716WfREPps2wdtvW0B09epJs89JDTp0sA73woVw7rmwc2ecKr7mGvP/3HOP++Od/XCBLyPvvGMumhtuiDjwxhsWIvnLXybFLif16NcPnnnGBlzjlkNexCpt2dIqTVM3p5MYEhkm+RowHThSRNaISKQD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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure()\n",
    "ax1 = sns.distplot(y_test, hist=False, color='blue', label = 'Y_test')\n",
    "sns.distplot(yhat, hist=False, color= 'red', label='Yhat', ax=ax1)\n",
    "plt.title('DADOS DE TESTE x PREVISÃO DO MODELO')\n",
    "plt.xlabel('Preço (in dollars)')\n",
    "plt.show()\n",
    "plt.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c15d0d6f-1576-4186-ba7b-a6b82f9ca6b0",
   "metadata": {},
   "source": [
    "Um gráfico de densidade dos dados de teste e a previsão do modelo e nota-se que eles se sobrepõe, tendo uma diferença entre os valores 2000 e 3000"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "62522943-edd0-4bad-bc0b-f98de4ea71f4",
   "metadata": {},
   "source": [
    "### Regressão linear múltipla"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "55bde60c-e26a-4452-a00b-aaf81ed92bdd",
   "metadata": {},
   "outputs": [],
   "source": [
    "z = df[['length','width','curb-weight','engine-size','horsepower','city-mpg','highway-mpg','wheel-base','bore','drive-wheels']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "188dec35-2262-44fb-a85f-de6a4684bf8c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['rwd', 'fwd', '4wd'], dtype=object)"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z['drive-wheels'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "d6719992-88ed-46ed-a7b3-253246c89552",
   "metadata": {},
   "outputs": [],
   "source": [
    "z['drive-wheels'] = z['drive-wheels'].map({'rwd':0, 'fwd':1, '4wd':2})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "26719e48-6b2e-4197-aa5d-c49fa3dfda61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Amostra teste: 71\n",
      "Amostra treino: 130\n"
     ]
    }
   ],
   "source": [
    "z_train, z_test, y_train, y_test = train_test_split(z, y, test_size=0.35, random_state=2)\n",
    "\n",
    "print('Amostra teste: {}'.format(z_test.shape[0]))\n",
    "print('Amostra treino: {}'.format(z_train.shape[0]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "83327d06-99b5-412c-aafc-b3e746701676",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = LinearRegression()\n",
    "model.fit(z, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "a01999b2-a670-4d40-aad7-b5d3e493d53e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 9090.80913138,  9405.49723302, 19471.55651863, 20753.11933334,\n",
       "        6404.1276922 ])"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p = model.predict(z_test)\n",
    "p[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "93551210-f2da-4245-974f-56c7e4e9ab17",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Score: 0.8157\n"
     ]
    }
   ],
   "source": [
    "print('Score: {:.4f}'.format(model.score(z_test, y_test)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "c121c83a-d8f3-4e4e-b00b-b9728af7631b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MSE: 3331.9527749990075\n"
     ]
    }
   ],
   "source": [
    "mse = mean_squared_error(y_test, p)\n",
    "print('MSE: {}'.format(np.sqrt(mse)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "db59881c-e148-4901-9547-40a7fd36ebb6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MSLE: 0.22370838796640471\n"
     ]
    }
   ],
   "source": [
    "msle = mean_squared_log_error(y_test, p)\n",
    "print('MSLE: {}'.format(np.sqrt(msle)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "473aa247-4999-4a89-9552-8f2895ad5006",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE: 2632.902638204569\n"
     ]
    }
   ],
   "source": [
    "mae = mean_absolute_error(y_test, p)\n",
    "print('MAE: {}'.format(mae))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "d7cc389a-5f0b-407b-9223-480e88f54895",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure()\n",
    "ax1 = sns.distplot(y_test, hist=False, color='blue', label = 'Y_test')\n",
    "sns.distplot(p, hist=False, color= 'red', label='Predict', ax=ax1)\n",
    "plt.title('DADOS DE TESTE x PREVISÃO DO MODELO')\n",
    "plt.xlabel('Preço (in dollars)')\n",
    "plt.show()\n",
    "plt.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b30cc314-f7dd-4c2b-9709-a08d366cc46a",
   "metadata": {},
   "source": [
    "## Random Forest Regressor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "adfb7b50-0ba6-43ef-b6dc-1d24f5492a31",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestRegressor(n_estimators=300, random_state=1)"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestRegressor\n",
    "\n",
    "rf = RandomForestRegressor(n_estimators=300, random_state=1)\n",
    "rf.fit(z_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "bf938b5b-105e-438a-ba5e-88b286bc0c8b",
   "metadata": {},
   "outputs": [],
   "source": [
    "predict = rf.predict(z_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "88e87e2e-87dc-453a-abb0-984ff2c819a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8516595853580493"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf.score(z_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "1130ef94-ee60-49c1-8b6b-3ebb50dcdbbc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MSE: 2989.3033789446736\n"
     ]
    }
   ],
   "source": [
    "mse = mean_squared_error(y_test, predict)\n",
    "print('MSE: {}'.format(np.sqrt(mse)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "20db708e-ae59-45bc-b5b8-0b2ac0008cbd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MSLE: 0.1876075714490047\n"
     ]
    }
   ],
   "source": [
    "msle = mean_squared_log_error(y_test, predict)\n",
    "print('MSLE: {}'.format(np.sqrt(msle)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "c31cd54f-dd09-4172-a335-a77ee2573592",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE: 2035.159712161861\n"
     ]
    }
   ],
   "source": [
    "mae = mean_absolute_error(y_test, predict)\n",
    "print('MAE: {}'.format(mae))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "4671b96b-d8c7-47d1-9f86-f420f1c98887",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure()\n",
    "ax1 = sns.distplot(y_test, hist=False, color='blue', label = 'Y_test')\n",
    "sns.distplot(predict, hist=False, color= 'red', label='Predict', ax=ax1)\n",
    "plt.title('DADOS DE TESTE x PREVISÃO DO MODELO')\n",
    "plt.xlabel('Preço (in dollars)')\n",
    "plt.show()\n",
    "plt.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68c13458-d959-40a9-b0c6-a36805cc8bd4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
