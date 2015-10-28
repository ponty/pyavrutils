from path import Path
from pyavrutils import support


docroot = Path('.') / 'docs'


# ARDUINO_VERSIONS = [
#     '0022',
#     #'0023',
#     '1.0',
# ]


# @task
# def build_test():
#     for ver in ARDUINO_VERSIONS:
#         os.environ['ARDUINO_HOME'] = path(
#             '~/opt/arduino-{0}'.format(ver)).expanduser()
#         csv = docroot / 'generated_build_test_{0}.csv'.format(ver)
#         support.build2csv(
#             [path('tests/min.pde')],
#             csv,
#             logdir=docroot / '_build' / 'html',
#             logger=info,
#         )


def buildcsv():
    csv = docroot / 'generated_build_test.csv'
    support.build2csv(
        [Path('tests/min.pde')],
        csv,
        logdir=docroot / 'log',
        logger=None,
    )
