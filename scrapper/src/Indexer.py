import os
import datetime
import Scrapper
import time

class indexer:

    def __init__(self,
                 scrap,
                 url,
                 area="",
                 sub_area="",
                 secretaria="",
                 departamento="",
                 ata_de_registro_de_preco="",
                 modalidade="",
                 status="",
                 numero_da_licitacao="",
                 numero_do_processo="",
                 publicacao_data_inicio="",
                 publicacao_data_fim="",
                 processo_data_inicio="",
                 processo_data_fim=""
                 ):
        self.scrap = scrap
        self.area = area
        self.sub_area = sub_area
        self.secretaria = secretaria
        self.departamento = departamento
        self.ata_de_registro_de_preco = ata_de_registro_de_preco
        self.modalidade = modalidade
        self.status = status
        self.numero_da_licitacao = numero_da_licitacao
        self.numero_do_processo = numero_do_processo
        self.publicacao_data_inicio = publicacao_data_inicio
        self.publicacao_data_fim = publicacao_data_fim
        self.processo_data_inicio = processo_data_inicio
        self.processo_data_fim = processo_data_fim
        self.scrap.driver.get(url)
        self.baseQueue = ["self.driver.get(\""+url+"\")"]

    def fill_field(self, field, value):
        if value != "":
            if field == "area":
                pass
            elif field == "sub_area":
                pass
            elif field == "secretaria":
                pass
            elif field == "departamento":
                pass
            elif field == "ata_de_registro_de_preco":
                pass
            elif field == "modalidade":
                pass
            elif field == "status":
                pass
            elif field == "numero_da_licitacao":
                pass
            elif field == "numero_do_processo":
                pass
            elif field == "publicacao_data_inicio":
                pass
            elif field == "publicacao_data_fim":
                pass
            elif field == "processo_data_inicio":
                pass
            elif field == "processo_data_fim":
                pass

    def fill_search_page(self):
        self.fill_field("area", self.area)
        self.fill_field("sub_area", self.sub_area)
        self.fill_field("secretaria", self.secretaria)
        self.fill_field("departamento", self.departamento)
        self.fill_field("ata_de_registro_de_preco",
                        self.ata_de_registro_de_preco)
        self.fill_field("modalidade", self.modalidade)
        self.fill_field("status", self.status)
        self.fill_field("numero_da_licitacao", self.numero_da_licitacao)
        self.fill_field("numero_do_processo", self.numero_do_processo)
        self.fill_field("publicacao_data_inicio", self.publicacao_data_inicio)
        self.fill_field("publicacao_data_fim", self.publicacao_data_fim)
        self.fill_field("processo_data_inicio", self.processo_data_inicio)
        self.fill_field("processo_data_fim", self.processo_data_fim)

    def search(self):
        self.baseQueue.append("self.driver.find_element_by_name('ctl00$cphConteudo$frmBuscaLicitacao$ibtBuscar').click()")

    def start_scrapping(self):
        for i in self.baseQueue:
            eval(i)
        while True:
            for i in range(5):
                s = Scrapper.scrapper(self.scrap.executable_path, self.scrap.options, action_queue=[])
                s.action_queue = self.baseQueue
                s.start()
            

