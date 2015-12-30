from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def documenation():
  return render_template('docs.html')

@app.route('/celsius', methods=['GET'])
def fahrenheit_to_celsius():
  fahrenheit = request.args['fahrenheit']
  is_input_a_number = is_number(fahrenheit)

  if is_input_a_number:
    celsius = (float() -32) * 5/9
    return 'celsius: ' + str(celsius)
  else:
    return "Invalid input: " + fahrenheit;


def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

if __name__ == '__main__':
  app.run(debug = True)
