# Logging function, output to file all.log.
import os
import logging
from logging import handlers


class RelativePathFormatter(logging.Formatter):
    def format(self, record):
        record.pathname = os.path.relpath(record.pathname)
        return super().format(record)


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename, level='info', when='D', backCount=7,  # Configurado para limpar o histórico antigo depois de 7 Dias
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        if not self.logger.hasHandlers():  # Verifica se o logger já possui handlers
            self.logger.setLevel(self.level_relations.get(level))
            th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                                   encoding='utf-8')
            format_str = RelativePathFormatter(fmt)
            th.setFormatter(format_str)
            self.logger.addHandler(th)


if __name__ == '__main__':
    log = Logger('all.log', level='debug')
    log.logger.debug('debug')
    log.logger.info('info')
    log.logger.warning('warn')
    log.logger.error('error')
    log.logger.critical('fatal')
    Logger('error.log', level='error').logger.error('error')
