import {Form, Button} from "react-bootstrap";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import oldPerson from "../assets/userData/oldPerson.png";
import youngPerson from "../assets/userData/youngPerson.png";
import noMoney from "../assets/userData/noMoney.png";
import muchMoney from "../assets/userData/muchMoney.png";

export default function UserData() {
    const [data, setData] = useState({
        age: 0,
        budget: 0,
        relationship: 0,
        occasion: "",
    });
    const navigate = useNavigate();

    const handleChange = (e) => {
        setData({ ...data, [e.target.name]: e.target.value });
    };

    const getRelationshipString = () => {
        if (data.relationship >= 0 && data.relationship <= 20) {
            return 'acquaintance';
        } else if (data.relationship >= 21 && data.relationship <= 40) {
            return 'friend';
        } else if (data.relationship >= 41 && data.relationship <= 60) {
            return 'good friend';
        } else if (data.relationship >= 61 && data.relationship <= 80) {
            return 'best friend';
        } else if (data.relationship >= 81 && data.relationship <= 100) {
            return 'more than a friend';
        }
        return ''
    }

    return (
        <Form className="p-4 border rounded">
            <h3>Your Data</h3>

            <Form.Group className="mb-3">
                <Form.Label column="sm">How old do you feel?</Form.Label>
                <div className="d-flex align-items-center">
                    <div className="selectionImage me-3">
                        <img src={youngPerson}  alt="youngPerson"/>
                    </div>
                    <Form.Range
                        name="age"
                        min={0}
                        max={100}
                        value={data.age}
                        onChange={handleChange}
                    />
                    <div className="selectionImage ms-3">
                        <img src={oldPerson} alt="oldPerson" />
                    </div>
                </div>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label column="sm">How much money would you like to spend?</Form.Label>
                <div className="d-flex align-items-center">
                    <div className="selectionImage me-3">
                        <img src={noMoney} alt="noMoney"/>
                    </div>
                    <Form.Range
                        name="budget"
                        min={0}
                        max={100}
                        value={data.budget}
                        onChange={handleChange}
                    />
                    <div className="selectionImage ms-3">
                        <img src={muchMoney} alt="muchMoney"/>
                    </div>
                </div>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label column="sm">The other person is a {getRelationshipString()}.</Form.Label>
                <div className="d-flex align-items-center">
                    <div className="selectionText me-3">
                        Not very close
                    </div>
                    <Form.Range
                        name="relationship"
                        min={0}
                        max={100}
                        value={data.relationship}
                        onChange={handleChange}
                    />
                    <div className="selectionText ms-3">
                        Very close
                    </div>
                </div>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label column="sm">Occasion</Form.Label>
                <Form.Select name="occasion" onChange={handleChange}>
                    <option value="">Select</option>
                    <option>Birthday</option>
                    <option>Anniversary</option>
                    <option>Graduation</option>
                    <option>Holiday</option>
                </Form.Select>
            </Form.Group>

            <Button onClick={() => navigate("/other")}>Next</Button>
        </Form>
    );
}
