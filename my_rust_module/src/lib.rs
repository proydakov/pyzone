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

/// Speeker
#[derive(Clone)]
#[pyclass]
struct Speeker {
    #[pyo3(get)]
    name: String,

    #[pyo3(get)]
    version: String,
}

/// Speeker
#[pymethods]
impl Speeker {
    #[new]
    fn new(name: String, version: String) -> Self {
        Speeker { name, version }
    }

    fn talk(&self) {
        println!("Talking [{}] with Speech version {}.", self.name, self.version);
    }
}

/// T800
#[pyclass]
struct T800 {
    speeker: Speeker,
    
    #[pyo3(get)] // Exposes this field as a Python property
    name: String,

    #[pyo3(get, set)] // Exposes this field as a Python property
    year: i32,
}

/// T800
#[pymethods]
impl T800 {
    #[new]
    fn new(name: String, year: i32, speeker: Speeker) -> Self {
        T800 { name, year, speeker }
    }

    fn walk(&self) {
        println!("T-800 is walking...");
    }

    fn talk(&self) {
        print!("{} ", self.name);
        self.speeker.talk();
    }
}

/// T1000
#[pyclass]
struct T1000 {
    speeker: Speeker,

    #[pyo3(get)] // Exposes this field as a Python property
    name: String,

    #[pyo3(get, set)] // Exposes this field as a Python property
    height: f64,
}

/// T1000
#[pymethods]
impl T1000 {
    #[new]
    fn new(name: String, height: f64, speeker: Speeker) -> Self {
        T1000 { name, height, speeker }
    }

    fn walk(&self) {
        println!("T-1000 is walking...");
    }

    fn talk(&self) {
        print!("{} ", self.name);
        self.speeker.talk();
    }
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

    // Add the classes to the module
    m.add_class::<Speeker>()?;
    m.add_class::<T800>()?;
    m.add_class::<T1000>()?;

    Ok(())
}
