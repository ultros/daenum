import subprocess
import openai


def enumerate_service(service_name):
    openai.api_key = ""

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="what is " + service_name,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response["choices"][0]['text']


def show_services():
    command = ["service", "--status-all"]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=None)
    data = process.stdout.decode().splitlines()
    for proc in data:
        item = proc.replace("[ - ]", '')
        item = item.replace("[ + ]", '').strip()
        print(f"{item} - {enumerate_service(item).strip()}\n")


def main():
    show_services()


if __name__ == '__main__':
    main()
