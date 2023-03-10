# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15, 2023 02:33:13 GMT+05:30

@author: PythonTrader
@licence: MIT
"""
import sys
import io
import os
import subprocess
import pkg_resources
import requests as rq
from pathlib import Path
from zipfile import ZipFile
from pkg_resources import DistributionNotFound, VersionConflict

__author__ = "Python Trader"
__webpage__ = "https://t.me/pythontrader"
__license__ = "MIT"


class PythonTrader:
    @staticmethod
    def should_install_requirement(requirement: str):
        should_install = False
        try:
            pkg_resources.require(requirement)
        except (DistributionNotFound, VersionConflict):
            should_install = True
        finally:
            return should_install

    @staticmethod
    def install_packages(requirement_list: list, _venv_path=None):
        try:
            requirements = [
                requirement
                for requirement in requirement_list
                if PythonTrader.should_install_requirement(requirement)
            ]
            if len(requirements) > 0:
                if _venv_path is None:
                    subprocess.check_call(
                        [sys.executable, "-m", "pip", "install", *requirements]
                    )
                else:
                    subprocess.check_call(
                        [_venv_path, "-m", "pip", "install", *requirements]
                    )
            else:
                print("Requirements Already Satisfied.")
        except Exception as Error:
            print(f"An Exception {Error} has occured while installing packages")

    @staticmethod
    def InstallZerodhaTradeTerminal(version: str):
        s = rq.session()
        try:
            import winshell
        except Exception as Error:
            print("Are You Sure The Packages 'winshell' Has Been Installed ?")
            print(
                f"An Exception {Error} has occured"
                + " while importing 'winshell' packages"  # noqa: E501
            )
            print("Install 'winshell' and retry again !")
            sys.exit(0)
        ztt_url = (
            "https://github.com/MooneDrJune/"
            + "ZTT_By_PythonTrader/releases/download"
            + f"/{version}/ZerodhaTradeTerminal.zip"
        )  # noqa: E501
        ztt_dir = os.path.join(
            Path(winshell.folder("profile")), "ZerodhaTradeTerminal"
        )  # noqa: E501
        os.makedirs(ztt_dir, exist_ok=True)
        with ZipFile(io.BytesIO(s.get(ztt_url).content)) as zttzip:
            zttzip.extractall(path=ztt_dir)

    @staticmethod
    def create_desktop_shortcut():
        try:
            import winshell
            import win32api
        except Exception as Error:
            print(
                "Are You Sure The Packages 'winshell' "
                + "& 'pywin32' Has Been Installed ?"  # noqa: E501
            )
            print(
                f"An Exception {Error} has occured while "
                + "importing 'winshell' & 'pywin32' packages"  # noqa: E501
            )
            print("Install 'winshell' & 'pywin32' and retry again !")
            sys.exit(0)
        win32_cmd = str(Path(winshell.folder("CSIDL_SYSTEM")) / "cmd.exe")
        pwsh = str(  # noqa: F841
            Path(winshell.folder("CSIDL_SYSTEM"))
            / "WindowsPowerShell"
            / "v1.0"
            / "powershell.exe"
        )
        desktop = Path(winshell.desktop())
        ztt_dir = os.path.join(
            Path(winshell.folder("profile")), "ZerodhaTradeTerminal"
        )  # noqa: E501
        ztt_icon = str(os.path.join(Path(ztt_dir), "PythonTrader.ico"))
        set_path = f"set PATH={ztt_dir}\\;%PATH%"
        ztt_dir = str(ztt_dir)
        ztt_code = f"/K {set_path} & python Zerodha_Trade_Terminal_V3_001.py"
        link_filepath = str(
            os.path.join(Path(desktop), "ZerodhaTradeTerminal.lnk")
        )  # noqa: E501
        with winshell.shortcut(link_filepath) as link:
            link.path = win32_cmd
            link.description = "ZerodhaTradeTerminal"
            link.arguments = ztt_code
            link.icon_location = (ztt_icon, 0)
            link.working_directory = ztt_dir

    @staticmethod
    def izttvacds(version: str):
        # Install Zerodha Trade Terminal Venv And Create Desktop Shortcut
        PythonTrader.InstallZerodhaTradeTerminal("V.0.3")
        PythonTrader.create_desktop_shortcut()


if __name__ == "__main__":
    MyPython = PythonTrader()
    MyPython.install_packages(["requests", "winshell", "pywin32"])
    MyPython.izttvacds("V.0.3")
