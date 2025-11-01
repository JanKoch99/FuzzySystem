import { Form, Button, Alert, Spinner } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import introvertedPerson from "../assets/otherPersonData/introvertedPerson.png"
import extrovertedPerson from "../assets/otherPersonData/extrovertedPerson.png"
import dataService from "../services/dataService";


export default function OtherPersonData() {
    const [data, setData] = useState({
        gender: "",
        personality: 0,
        technical: 0,
        creative: 0,
        managerial: 0,
        academic: 0,
        style: "Classic",
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const handleChange = (e) => {
        setData({ ...data, [e.target.name]: e.target.value });
    }

    const handleNext = async () => {
        setError("");
        setLoading(true);
        try {
            dataService.setOtherPersonData(data);
            await dataService.fetchImagePairs();
            navigate("/images");
        } catch (e) {
            setError(e.message || "Failed to load image pairs");
        } finally {
            setLoading(false);
        }
    }

    return (
        <Form className="p-4 border rounded">
            <h3>Other Person’s Data</h3>

            <Form.Group className="mb-3">
                <Form.Label column="sm">What is the other persons gender?</Form.Label>
                <Form.Select name="gender" onChange={handleChange}>
                    <option value="">Select</option>
                    <option>Male</option>
                    <option>Female</option>
                </Form.Select>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label column="sm">Would you describe the other person as introvert or extrovert?</Form.Label>
                <div className="d-flex align-items-center">
                    <div className="selectionImage me-3">
                        <img src={introvertedPerson}  alt="introvertedPerson"/>
                    </div>
                    <Form.Range
                        name="personality"
                        min={0}
                        max={100}
                        value={data.personality}
                        onChange={handleChange}
                    />
                    <div className="selectionImage ms-3">
                        <img src={extrovertedPerson} alt="extrovertedPerson" />
                    </div>
                </div>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label column="sm">Technical</Form.Label>
                <div className="d-flex align-items-center">
                    <div className="selectionText me-3">
                        Not very technical
                    </div>
                    <Form.Range
                        name="technical"
                        min={0}
                        max={100}
                        value={data.technical}
                        onChange={handleChange}
                    />
                    <div className="selectionText ms-3">
                        Very technical
                    </div>
                </div>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label column="sm">Creative</Form.Label>
                <div className="d-flex align-items-center">
                    <div className="selectionText me-3">
                        Not very creative
                    </div>
                    <Form.Range
                        name="creative"
                        min={0}
                        max={100}
                        value={data.creative}
                        onChange={handleChange}
                    />
                    <div className="selectionText ms-3">
                        Very creative
                    </div>
                </div>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label column="sm">Managerial</Form.Label>
                <div className="d-flex align-items-center">
                    <div className="selectionText me-3">
                        Not very managerial
                    </div>
                    <Form.Range
                        name="managerial"
                        min={0}
                        max={100}
                        value={data.managerial}
                        onChange={handleChange}
                    />
                    <div className="selectionText ms-3">
                        Very managerial
                    </div>
                </div>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label column="sm">Academic</Form.Label>
                <div className="d-flex align-items-center">
                    <div className="selectionText me-3">
                        Not very academic
                    </div>
                    <Form.Range
                        name="academic"
                        min={0}
                        max={100}
                        value={data.academic}
                        onChange={handleChange}
                    />
                    <div className="selectionText ms-3">
                        Very academic
                    </div>
                </div>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label column="sm">Style</Form.Label>
                <Form.Select name="style" value={data.style} onChange={handleChange}>
                    <option value="">Select</option>
                    <option>Classic</option>
                    <option>Modern</option>
                    <option>Trendy</option>
                    <option>Minimalist</option>
                </Form.Select>
            </Form.Group>

            {error && (
                <Alert variant="danger" className="mb-3">{error}</Alert>
            )}

            <Button onClick={() => navigate("/user")} className="me-4">Previous</Button>

            <Button onClick={handleNext} disabled={loading}>
                {loading && <Spinner as="span" animation="border" size="sm" role="status" aria-hidden="true" className="me-2" />}
                {loading ? "Loading..." : "Next"}
            </Button>
        </Form>
    );
}
