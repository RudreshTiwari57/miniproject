from behave.model import *
from tests.utilities.global_utiles import *

def before_scenario(context,scenario):
    logger.info(f"Staring scenario: {scenario.name}")
def before_step(context,step):
    logger.info(f"Starting step: {step.name}")


def after_step(context,step):

    if step.status == "failed":
        tb = "".join(traceback.format_exception(None,step.exception,step.exception.__traceback__))
        error_message = f"Step failed: {step.name}\n Error: {step.exception}\n Traceback: {tb}"
        logger.error(error_message)

    else:
        logger.info(f"Step passed: {step.name}")

def afer_scenario(context,scenario):
    if scenario.status == "failed":
        tb = None
        if Scenario.steps:
            for step in scenario.steps:
                if step.status=="failed":
                    tb = "".join(traceback.format_exception(None, step.exception, step.exception.__traceback__))
                    break
        if tb:
            error_message = f"Step failed: {step.name}\n Error: {step.exception}\n Traceback: {tb}"
            logger.error(error_message)
    else:
        logger.info(f"Step passed: {scenario.name}")
