from behave import given, when, then

def is_it_friday(today):
    if today == "Friday":
        return "TGIF"
    else:
        return "Nope"

@given('today is {day}')
def step_given_day(context, day):
    context.today = day
    print(f'Given: today is "{day}"')  # Adicionando instrução de impressão

@when("I ask whether it's Friday yet")
def step_ask_if_friday(context):
    context.actualAnswer = is_it_friday(context.today)
    print(f'When: I ask whether it\'s Friday yet, actualAnswer is "{context.actualAnswer}"')  # Adicionando instrução de impressão

@then('I should be told {answer}')
def step_should_be_told(context, answer):
    assert context.actualAnswer == answer
    print(f'Then: I should be told "{answer}", actualAnswer is "{context.actualAnswer}"')  # Adicionando instrução de impressão
