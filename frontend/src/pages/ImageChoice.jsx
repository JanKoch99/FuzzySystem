import { useMemo, useState } from "react";
import { Row, Col, Image, Alert, Button } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import dataService from "../services/dataService";

export default function ImageChoice() {
    const navigate = useNavigate();
    const pairs = useMemo(() => dataService.getImagePairs() || [], []);
    const [round, setRound] = useState(0);
    const [data, setData] = useState({
        image0: "",
        image1: "",
        image2: "",
        image3: "",
        image4: "",
    })

    if (!pairs || pairs.length === 0) {
        return (
            <div className="text-center">
                <Alert variant="warning" className="mt-3">
                    No image pairs available. Please provide data again.
                </Alert>
                <Button className="mt-2" onClick={() => navigate("/other")}>Back</Button>
            </div>
        );
    }

    const totalRounds = pairs.length;

    const handleChoice = async (e) => {
        await setData({...data, [`image${round}`]: e})
        if (round < totalRounds - 1) {
            setRound(round + 1)
        } else {
            dataService.setSelectedImagePairs(data)
            await dataService.fetchFinalImages()
            dataService.clear()
            navigate("/suggestion")
        }
    };

    return (
        <div className="text-center">
            <h3>Choose your preferred gift (Round {round + 1}/{totalRounds})</h3>
            <Row className="mt-4">
                <Col>
                    <Image
                        src={pairs[round][0].path}
                        thumbnail
                        style={{ cursor: "pointer" }}
                        onClick={() => handleChoice(pairs[round][0].value)}
                    />
                </Col>
                <Col>
                    <Image
                        src={pairs[round][1].path}
                        thumbnail
                        style={{ cursor: "pointer" }}
                        onClick={() => handleChoice(pairs[round][1].value)}
                    />
                </Col>
            </Row>
        </div>
    );
}
