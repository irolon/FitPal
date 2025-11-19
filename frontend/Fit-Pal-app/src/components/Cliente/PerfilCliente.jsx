import { useEffect, useMemo, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import "../../css/perfilCliente.css";

const API_BASE = import.meta.env.VITE_API_URL;

const PerfilCliente = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    nombre: "",
    apellido: "",
    correo: "",
    dni: "",
    edad: "",
    fecha_inicio: "",
    rol: "cliente",
    contrasena: "",
  });
  const [initialFormData, setInitialFormData] = useState(null);

  const [planes, setPlanes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  useEffect(() => {
    const controller = new AbortController();

    const fetchProfile = async () => {
      if (!id) {
        setError("No encontramos el usuario seleccionado.");
        setLoading(false);
        return;
      }

      setLoading(true);
      setError("");

      try {
        const [usuarioRes, clienteRes, planesRes] = await Promise.all([
          fetch(`${API_BASE}/api/usuarios/${id}`, { signal: controller.signal }),
          fetch(`${API_BASE}/api/clientes/${id}`, { signal: controller.signal }),
          fetch(`${API_BASE}/api/cliente/${id}/planes`, {
            signal: controller.signal,
          }),
        ]);

        if (!usuarioRes.ok) {
          throw new Error("No pudimos obtener los datos del usuario.");
        }

        const usuario = await usuarioRes.json();

        if (!clienteRes.ok) {
          throw new Error("No pudimos obtener los datos del cliente.");
        }

        const cliente = await clienteRes.json();

        let planesParsed = [];
        if (planesRes.ok) {
          const planesData = await planesRes.json();
          planesParsed = Array.isArray(planesData) ? planesData : [];
        }

        setPlanes(planesParsed);
        const nextFormData = {
          nombre: usuario.nombre ?? "",
          apellido: usuario.apellido ?? "",
          correo: usuario.correo ?? "",
          dni: cliente.dni ?? "",
          edad: cliente.edad?.toString() ?? "",
          fecha_inicio: cliente.fecha_inicio?.split("T")[0] ?? cliente.fecha_inicio ?? "",
          rol: usuario.rol ?? "cliente",
          contrasena: usuario.contrasena ?? "",
        };
        setFormData(nextFormData);
        setInitialFormData({ ...nextFormData });
      } catch (err) {
        if (err.name === "AbortError") return;
        console.error(err);
        setError(err.message || "Ocurrió un error al traer tu información.");
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();

    return () => controller.abort();
  }, [id]);

  const displayData = initialFormData || formData;

  const avatarUrl = useMemo(() => {
    const label = `${displayData.nombre} ${displayData.apellido}`.trim() || "Fit Pal";
    const encoded = encodeURIComponent(label);
    return `https://ui-avatars.com/api/?name=${encoded}&background=1b1b1b&color=fff`;
  }, [displayData.nombre, displayData.apellido]);

  const resumenPreferencias = useMemo(() => {
    if (!planes.length) {
      return {
        titulo: "Sin plan activo",
        frecuencia: "Aún no tienes una planificación asignada.",
        fechas: "Contactá a tu coach para obtener tu primer plan.",
      };
    }

    const planActual = planes[0];
    const frecuenciaSemana = Number(planActual.frecuencia) || planActual.frecuencia;
    const fechaInicio = planActual.fecha_inicio
      ? new Date(planActual.fecha_inicio).toLocaleDateString()
      : "-";
    const fechaFin = planActual.fecha_fin
      ? new Date(planActual.fecha_fin).toLocaleDateString()
      : "-";

    return {
      titulo: planActual.nombre,
      frecuencia: typeof frecuenciaSemana === "number"
        ? `${frecuenciaSemana} sesiones / semana`
        : `${planActual.frecuencia}`,
      fechas: `Del ${fechaInicio} al ${fechaFin}`,
    };
  }, [planes]);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!id) return;

    const requiredFields = ["nombre", "apellido", "correo", "dni", "edad", "fecha_inicio"];
    const hasEmpty = requiredFields.some((field) => {
      const value = formData[field];
      return value === undefined || value === null || `${value}`.trim() === "";
    });
    if (hasEmpty) {
      setError("Por favor completá todos los campos antes de guardar.");
      return;
    }

    setSaving(true);
    setError("");
    setSuccess("");

    try {
      const usuarioPayload = {
        nombre: formData.nombre,
        apellido: formData.apellido,
        correo: formData.correo,
        contrasena: formData.contrasena,
        rol: formData.rol || "cliente",
      };

      const clientePayload = {
        nombre: formData.nombre,
        apellido: formData.apellido,
        correo: formData.correo,
        contrasena: formData.contrasena,
        dni: formData.dni,
        edad: Number(formData.edad) || 0,
        fecha_inicio: formData.fecha_inicio,
      };

      const [usuarioRes, clienteRes] = await Promise.all([
        fetch(`${API_BASE}/api/usuarios/${id}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(usuarioPayload),
        }),
        fetch(`${API_BASE}/api/clientes/${id}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(clientePayload),
        }),
      ]);

      if (!usuarioRes.ok || !clienteRes.ok) {
        throw new Error("No pudimos guardar los cambios. Intentalo nuevamente.");
      }

      setSuccess("Tu perfil se actualizó correctamente.");
      setInitialFormData({
        nombre: formData.nombre,
        apellido: formData.apellido,
        correo: formData.correo,
        dni: formData.dni,
        edad: formData.edad,
        fecha_inicio: formData.fecha_inicio,
        rol: formData.rol,
        contrasena: formData.contrasena,
      });

      const storedUser = localStorage.getItem("user");
      if (storedUser) {
        try {
          const parsed = JSON.parse(storedUser);
          const updatedUser = {
            ...parsed,
            nombre: formData.nombre,
            correo: formData.correo,
          };
          localStorage.setItem("user", JSON.stringify(updatedUser));
        } catch {
          // Ignoramos si el JSON es inválido, sólo evitamos romper el flujo.
        }
      }
    } catch (err) {
      console.error(err);
      setError(err.message || "Ocurrió un problema al guardar tus cambios.");
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
    return (
      <div className="perfil-container d-flex align-items-center justify-content-center min-vh-100">
        <div className="spinner-border text-light" role="status">
          <span className="visually-hidden">Cargando...</span>
        </div>
      </div>
    );
  }

  return (
    <div className="perfil-container py-5 min-vh-100">
      <div className="container">
        <div className="d-flex align-items-center justify-content-between mb-4 flex-wrap gap-3">
          <div>
            <p className="perfil-breadcrumb mb-1">
              <Link to="/cliente" className="perfil-link">Panel cliente</Link> / Mi perfil
            </p>
            <h1 className="perfil-title">Mi perfil</h1>
          </div>
          <button className="btn btn-dark" onClick={() => navigate(-1)}>
            Volver
          </button>
        </div>

        {error && <div className="alert alert-danger">{error}</div>}
        {success && <div className="alert alert-success">{success}</div>}

        <div className="row g-4">
          <div className="col-12 col-lg-4">
            <div className="perfil-card h-100 text-center">
              <img src={avatarUrl} alt="Avatar del cliente" className="perfil-avatar mb-3" />
              <h2 className="perfil-name">{displayData.nombre} {displayData.apellido}</h2>
              <p className="perfil-mail">{displayData.correo}</p>

              <div className="perfil-meta mt-4">
                <div>
                  <span className="perfil-meta-label">DNI</span>
                  <p className="perfil-meta-value">{displayData.dni || "-"}</p>
                </div>
                <div>
                  <span className="perfil-meta-label">Edad</span>
                  <p className="perfil-meta-value">{displayData.edad || "-"}</p>
                </div>
                <div>
                  <span className="perfil-meta-label">Activo desde</span>
                  <p className="perfil-meta-value">
                    {displayData.fecha_inicio
                      ? new Date(displayData.fecha_inicio).toLocaleDateString()
                      : "-"}
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div className="col-12 col-lg-8">
            <div className="perfil-card h-100">
              <div className="d-flex align-items-center justify-content-between mb-3 flex-wrap gap-2">
                <div>
                  <h2 className="perfil-section-title mb-1">Datos personales</h2>
                  <p className="perfil-section-subtitle">Mantené tu información siempre actualizada.</p>
                </div>
                <button
                  className="btn btn-dark"
                  type="button"
                  onClick={() => initialFormData && setFormData({ ...initialFormData })}
                  disabled={!initialFormData || saving}
                >
                  Reiniciar datos
                </button>
              </div>

              <form onSubmit={handleSubmit} className="row g-3">
                <div className="col-md-6">
                  <label className="form-label">Nombre</label>
                  <input
                    type="text"
                    name="nombre"
                    className="form-control"
                    value={formData.nombre}
                    onChange={handleInputChange}
                    required
                  />
                </div>
                <div className="col-md-6">
                  <label className="form-label">Apellido</label>
                  <input
                    type="text"
                    name="apellido"
                    className="form-control"
                    value={formData.apellido}
                    onChange={handleInputChange}
                    required
                  />
                </div>
                <div className="col-md-6">
                  <label className="form-label">Correo</label>
                  <input
                    type="email"
                    name="correo"
                    className="form-control"
                    value={formData.correo}
                    onChange={handleInputChange}
                    required
                  />
                </div>
                <div className="col-md-6">
                  <label className="form-label">DNI</label>
                  <input
                    type="text"
                    name="dni"
                    className="form-control"
                    value={formData.dni}
                    onChange={handleInputChange}
                    required
                  />
                </div>
                <div className="col-md-6">
                  <label className="form-label">Edad</label>
                  <input
                    type="number"
                    name="edad"
                    min="0"
                    className="form-control"
                    value={formData.edad}
                    onChange={handleInputChange}
                    required
                  />
                </div>
                <div className="col-md-6">
                  <label className="form-label">Fecha de inicio</label>
                  <input
                    type="date"
                    name="fecha_inicio"
                    className="form-control"
                    value={formData.fecha_inicio || ""}
                    onChange={handleInputChange}
                    required
                  />
                </div>

                <div className="col-12 text-end">
                  <button className="btn btn-dark btn-lg" type="submit" disabled={saving}>
                    {saving ? "Guardando..." : "Guardar cambios"}
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>

        <div className="row g-4 mt-1">
          <div className="col-12 col-lg-6">
            <div className="perfil-card h-100">
              <h2 className="perfil-section-title mb-2">Preferencias de entrenamiento</h2>
              <p className="perfil-section-subtitle">{resumenPreferencias.titulo}</p>
              <div className="perfil-preferencias">
                <div>
                  <span className="perfil-meta-label">Frecuencia</span>
                  <p className="perfil-meta-value">{resumenPreferencias.frecuencia}</p>
                </div>
                <div>
                  <span className="perfil-meta-label">Vigencia</span>
                  <p className="perfil-meta-value">{resumenPreferencias.fechas}</p>
                </div>
              </div>
              <Link to={`/cliente/${id}/planes`} className="btn btn-outline-dark mt-3">
                Ver planes asignados
              </Link>
            </div>
          </div>

          <div className="col-12 col-lg-6">
            <div className="perfil-card h-100">
              <h2 className="perfil-section-title mb-2">Sesiones y avance</h2>
              <p className="perfil-section-subtitle">
                Accedé a tus sesiones para registrar tu progreso diario.
              </p>
              <div className="perfil-progreso">
                <div>
                  <span className="perfil-meta-label">Sesiones del plan</span>
                  <p className="perfil-meta-value">
                    {planes.length > 0
                      ? `${(Number(planes[0].frecuencia) || 0) * 4} aprox / mes`
                      : "Sin datos"}
                  </p>
                </div>
                <div>
                  <span className="perfil-meta-label">Planes activos</span>
                  <p className="perfil-meta-value">{planes.length}</p>
                </div>
              </div>
              <Link to={`/cliente/${id}/sesiones`} className="btn btn-outline-dark mt-3">
                Ir a mis sesiones
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PerfilCliente;
