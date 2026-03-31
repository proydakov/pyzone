use pyo3::prelude::*;

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

/// A Python module implemented in Rust.
#[pymodule]
fn my_rust_module(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    // Add the functions to the module
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(greet, m)?)?;
    Ok(())
}
