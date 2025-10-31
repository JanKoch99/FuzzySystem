import { Form, Button } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import { useState } from "react";

export default function OtherPersonData() {
    const [data, setData] = useState({});
    const navigate = useNavigate();

    const handleChange = (e) =>
        setData({ ...data, [e.target.name]: e.target.value });

    return (
        <Form className="p-4 border rounded">
            <h3>Other Person’s Data</h3>

            <Form.Group className="mb-3">
                <Form.Label column="sm">Gender</Form.Label>
                <Form.Select name="gender" onChange={handleChange}>
                    <option value="">Select</option>
                    <option>Male</option>
                    <option>Female</option>
                    <option>Non-Binary</option>
                </Form.Select>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label column="sm">Personality Type</Form.Label>
                <Form.Select name="personality" onChange={handleChange}>
                    <option value="">Select</option>
                    <option>Introvert</option>
                    <option>Extrovert</option>
                    <option>Creative</option>
                    <option>Analytical</option>
                </Form.Select>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label column="sm">Lifestyle</Form.Label>
                <Form.Select name="lifestyle" onChange={handleChange}>
                    <option>Active</option>
                    <option>Relaxed</option>
                    <option>Adventurous</option>
                    <option>Homebody</option>
                </Form.Select>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label column="sm">Occupation</Form.Label>
                <Form.Control name="occupation" onChange={handleChange} />
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label column="sm">Style</Form.Label>
                <Form.Select name="style" onChange={handleChange}>
                    <option>Classic</option>
                    <option>Modern</option>
                    <option>Trendy</option>
                    <option>Minimalist</option>
                </Form.Select>
            </Form.Group>

            <Button onClick={() => navigate("/images")}>Next</Button>
        </Form>
    );
}
