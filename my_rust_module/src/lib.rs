use pyo3::prelude::*;
use pyo3::types::PyBytes;
use pyo3::types::PyByteArray;

/// A Rust function exposed to Python that adds two numbers and returns the result as a string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// A Rust function that returns a greeting string.
#[pyfunction]
fn greet(name: &str) -> PyResult<String> {
    Ok(format!("Hello, {}!", name))
}

/// Say some string.
#[pyfunction]
fn say(name: &str) {
    println!("{}", name);
}

/// Method with a bytes input.
#[pyfunction]
fn handle_bytes(bytes: &Bound<'_, PyBytes>) {
    println!("handle bytes [{}]", bytes.len().unwrap());
}

/// Method with a bytearray input.
#[pyfunction]
fn handle_bytearray(bytes: &Bound<'_, PyByteArray>) {
    println!("handle bytearray [{}]", bytes.len());
}

/// A Python module implemented in Rust.
#[pymodule]
fn my_rust_module(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    // Add the functions to the module
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(greet, m)?)?;
    m.add_function(wrap_pyfunction!(say, m)?)?;
    m.add_function(wrap_pyfunction!(handle_bytes, m)?)?;
    m.add_function(wrap_pyfunction!(handle_bytearray, m)?)?;
    Ok(())
}
