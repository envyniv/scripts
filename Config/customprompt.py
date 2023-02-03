#!/usr/bin/env python

from colorama import Fore, Back, Style
from rich import print
from getpass import getuser
from sys import argv
from os import getcwd, remove, environ, readlink
from os.path import exists
import git, re

from typing import List

special_folders = {
  readlink(environ["XDG_CONFIG_HOME"]) : " ",
  environ["XDG_DESKTOP_DIR"]           : " ",
  environ["XDG_PICTURES_DIR"]          : " ",
  environ["XDG_PUBLICSHARE_DIR"]       : " ",
  environ["XDG_TEMPLATES_DIR"]         : " ",
  environ["XDG_MUSIC_DIR"]             : " ",
  environ["XDG_DOWNLOAD_DIR"]          : " ",
  environ["XDG_DOCUMENTS_DIR"]         : " ",
  environ["XDG_VIDEOS_DIR"]            : " ",
  environ["HOME"]                      : " ",
}

folder_colors = dict(
# BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, LIGHTBLACK_EX,
# LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX,
# LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX
  red = "lightred_ex",
  black = "black",
  blue = "blue",
  brown = "lightblack_ex",
  bluegrey = "lightblack_ex",
  carmine = "red",
  cyan = "lightcyan_ex",
  darkcyan = "cyan",
  deeporange = "orange",
  green = "green",
  grey = "lightwhite_ex",
  indigo = "blue",
  magenta = "magenta",
  orange = "yellow",
  palebrown = "lightyellow_ex",
  paleorage = "lightyellow_ex",
  pink = "lightmagenta_ex",
  teal = "lightgreen_ex",
  violet = "magenta",
  white = "white",
  yellow = "yellow",
  
  nordic = "lightwhite_ex",
  breeze = "cyan",
  adwaita = "lightcyan_ex",
  yaru = "black",
)

class BasicPromptSection: # generic class for prompt sections
  text: str  = ""
  bgClr: str = ""
  fgClr: str = ""
  style: str = ""

  def getANSI(self, string: str, which: str = "f"):
    if string:
      match which:
        case "f": # foreground
          return getattr(Fore, string.upper())
        case "b": # background
          return getattr(Back, string.upper())
        case "s":
          return getattr(Style, string.upper())
    else:
      return ""

  def sanityCheck(self) -> None:
    """
    Ensures the foreground color doesn't match the background color,
    as to not have unreadable text.
    Could be expanded to 
    """
    if (self.bgClr == self.fgClr):
      self.fgClr = ""
      self.style = "bright"
    return

  def __init__(self, **kwargs) -> None:
    for key, val in kwargs.items():
      setattr(self, key, val)
    return

  def __str__(self) -> str:
    self.sanityCheck()
    return (self.getANSI(self.style, "s") + # style
          self.getANSI(self.fgClr) +      # foreground color
          self.getANSI(self.bgClr, "b") + # background color
          self.text + Style.RESET_ALL)

class PromptSection(BasicPromptSection): 
  sep_left: str  = "" # left separator character
  sep_lbgc: str  = "" # left separator bg color
  sep_right: str = "" # right separator character
  sep_rbgc: str  = "" # right separator bg color

  def __str__(self) -> str:
    return ((self.getANSI(self.bgClr) +
          self.getANSI(self.sep_lbgc, "b")
          + self.sep_left + Style.RESET_ALL) + 
          BasicPromptSection.__str__(self) + 
          (self.getANSI(self.bgClr) +
           self.getANSI(self.sep_rbgc, "b") +
           self.sep_right + Style.RESET_ALL))

username = getuser()
path = getcwd()

class PwdPromptSect(PromptSection):
  def is_git_repo(self, path) -> bool:
    try:
      _ = git.Repo(path, search_parent_directories=True).git_dir #black hole
      return True
    except git.exc.InvalidGitRepositoryError:
      return False

  def get_svsys(self, path):
    return

  def get_dir_color(self, path) -> str:
    text: str
    if exists(path+"/.directory"):
      with open(path+"/.directory") as iconfile:
        text = iconfile.read().split("\n")[1]
        for color in folder_colors:
          if (color in text):
            iconfile.close()
            return folder_colors[color]
    return ""
  
  def __init__(self, **kwargs) -> None:
    parsed_path = path
    for element in special_folders:
      if element in path:
        parsed_path = parsed_path.replace(
          element, special_folders[element]
        )
        break
    self.text = parsed_path

    if self.is_git_repo(path):
      self.bgClr = "lightred_ex"
      # self.text +=
    else:
      self.bgClr = "lightblack_ex"

    self.fgClr = self.get_dir_color(path)
    
    PromptSection.__init__(self, **kwargs)
    return

class CmdAtHstLine(PromptSection):
  def __init__(self):
    if exists(environ["HISTFILE"]):
      with open(environ["HISTFILE"]) as file:
        self.text = f"@{len(file.readlines())}"
        file.close()
    else:
      self.text = "@?"
    return

class VanillaPrompt(PromptSection):
  def __init__(self) -> None:
    # set prompt text
    if (argv[1] == "0"):
      self.fgClr = "green"
    else:
      self.fgClr = "red"
    self.text = "$"
    self.style = "bright"
    
    PromptSection.__str__(self)
    return

"""
class ResultPrompt(PromptSection):

  def get_time(self) -> str:
    time = 0
    if (exists(argv[2])):
      with open(argv[2]) as stmpfile:
        time = int(stmpfile.read())
        stmpfile.close()
      remove(argv[2])
          
      return str(time)
    else:
      return "file not found"

  def __init__(self) -> None:
    if (argv[1] == "1"):
      self.text = self.getColorProper("red")
    else:
      self.text = self.getColorProper("green")
    self.text += self.get_time()
    
    PromptSection.__init__(self, txt = self.text, st = "bright")
    return
"""

class PromptList():
  def __init__(self, *args) -> None:
    for index, elem in enumerate(args):
      if (index<(len(args)-1)):
        elem.sep_rbgc = args[index+1].bgClr
      print("\1"+str(elem)+"\2", end = "")
    return

PromptList(
  PromptSection(
          sep_left = "",
          text = username,
          sep_right = "",
          bgClr = "magenta",
          st = "bright"
         ),
  PwdPromptSect(sep_left = "", sep_right = ""),
  BasicPromptSection(text="\n"),
  # CmdAtHstLine(),
  # BasicPromptSection(),
  VanillaPrompt(),
)

exit()
