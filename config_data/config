from dataclasses import dataclass

from environs import Env

@dataclass

class TgBot:

    token: str

    chats: list[int]

@dataclass

class TCSClient:

    token: str   

@dataclass

class Config:

    tcs_client: TCSClient

    tg_bot: TgBot

def load_config(path: str = None) -> Config:

    env: Env = Env()

    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('TG_5MIN_TOKEN'), chats=list(map(int, env.list('CHATS')))),

                  tcs_client=TCSClient(token=env('TCS_TOKEN')))

                                    
