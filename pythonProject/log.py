# -*- coding: utf-8 -*-            
# @Author : 测试小牛
# @Time : 03/09/2023 11:42
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.debug("This is a debug message")DEBUG 级别：最详细的日志级别，用于调试和追踪程序执行的细节。
# logging.info("This is an info message")INFO 级别：用于输出程序运行过程中的一般信息，对程序的运行状态进行监控。
# logging.warning("This is a warning message")WARNING 级别：用于输出警告信息，表示程序可能存在潜在的问题，但不会影响程序的正常执行。
# logging.error("This is an error message")ERROR 级别：用于输出错误信息，表示程序发生了错误，但不影响程序的继续运行。
# logging.critical("This is a critical message")CRITICAL 级别：最高级别的日志，表示程序发生了严重的错误，可能导致程序无法继续运行。

logging.debug('请求入参')
logging.debug('返回报文')

