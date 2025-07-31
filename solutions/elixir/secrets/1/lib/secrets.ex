defmodule Secrets do
  def secret_add(secret) do
    function_variable = fn param ->
      param + secret
    end
  end

  def secret_subtract(secret) do
    function_variable = fn param ->
      param - secret
    end
  end

  def secret_multiply(secret) do
    function_variable = fn param ->
      param * secret
    end
  end

  def secret_divide(secret) do
    function_variable = fn param ->
      div(param, secret) 
    end
  end

  def secret_and(secret) do
    function_variable = fn param ->
      Bitwise.band(param, secret)
    end
  end

  def secret_xor(secret) do
    function_variable = fn param ->
      Bitwise.bxor(param, secret)
    end
  end

  def secret_combine(secret_function1, secret_function2) do
     &(&1 |> then(secret_function1) |> then(secret_function2))
  end
end
