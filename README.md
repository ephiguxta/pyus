### pyus

### Como utilizar

Na IDE do Arduino, utilize o atalho `Crtl + LShift + i` e procure pela biblioteca
"MAX6675 library" da Adafruit e instale a mesma.

Vá para o seu emulador de terminal ou cmd no Windows e crie um ambiente virtual:

`python -m venv env`


Na distro linux que estiver utilizando, ative o ambiente:

`source env/bin/activate`

Se estiver usando Windows, a ativação é feita através do script em bat:

`env\Scripts\activate.bat`

Agora com o ambiente ativo, instale a biblioteca **pyserial**:

`python -m pip install pyserial`

Depois de configurar tudo, suba o código para o arduino, deixe a IDE aberta e volte
para o cmd, digite `python get_data.py` e terá os logs em tela, arquivos de log também
serão gerados para guardar os dados.
