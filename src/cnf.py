"""
Simple CLI for finding the correct installation for a command.

Uses data from command-not-found.com.

"""

__version__ = "1.0.0"
__credits__ = "command-not-found.com"


import bs4
import dataclasses
import http
import platform
import requests
import subprocess
import sys


CNF_URL = 'https://command-not-found.com/'
CNF_TABLE_CLASS = 'row mb-0'

PRIORITY_PLATFORM_MATCHERS = (
  platform.version(),
  platform.platform(),
  platform.system(),
)

PLATFORM_PATCHES = {
  'OS X': 'macOS'
}

DOCS = """
Usage: cnf <command>

  command: Any command to find an installation for.

E.g cnfcli lsof
"""


class BadArgumentsError(Exception):
  ...


class FailedRequestError(Exception):
  ...


class UnknownCommandException(Exception):
  ...


@dataclasses.dataclass
class CliArgs():
  command: str
  
  @classmethod
  def parse(cls):
    try:
      return cls(*sys.argv[1:])
    except:
      raise BadArgumentsError


def get_platform(platforms):
  for this_platform in PRIORITY_PLATFORM_MATCHERS: 
    for platfrm in platforms:
      if platfrm in this_platform:
        return platfrm


def get_results(command):
  response = requests.get(CNF_URL + command) 
  if response.status_code != http.HTTPStatus.OK:
    raise FailedRequestError
  dom = bs4.BeautifulSoup(response.content, 'html.parser')
  table = dom.find('dl', {'class': CNF_TABLE_CLASS})
  if not table:
    raise UnknownCommandException
  results = {}
  for result in table.children:
    try:
      os = result['data-os']
    except (TypeError, KeyError):
      continue
    results[PLATFORM_PATCHES.get(os, os)] = result.find('code').text
  return results


def show_results(results):
  print()
  for platform, command in results.items():
    print(f'{platform}: {command}')
  print('\nSorry, couldn\'t work out which to use.')


def handle_command(command):
  print(f'Found `{command}`')
  run = (input(
    '\nWould you like to install it? [Y/n]').lower() or 'y') == 'y'
  if run:
    print('Installing (could take a while)...')
    output = subprocess.run(
      ['sudo'] + command.split(' '),
      capture_output=True,
      text=True).stdout
    print(output)


def nice_error(msg):
  print(msg)
  exit()


def main():
  try:
    args = CliArgs.parse()
  except:
    nice_error(f'Bad arguments provided. \n{DOCS}')
  try:
    results = get_results(args.command)  
  except UnknownCommandException:
    nice_error('Unknown command!')  
  except FailedRequestError:
    nice_error('Unknown Error!')
  platform = get_platform(results)
  if platform:
    handle_command(results[platform])
  else:
    show_results(results)


if __name__ == '__main__':
  main()
