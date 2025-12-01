import { Row, Col, Image } from "react-bootstrap";
import { useMemo } from "react";
import dataService from "../services/dataService.js";
import { getImageSrc } from "../utils/imageHelper";

export default function FinalSuggestion() {
  const images = useMemo(() => dataService.getFinalImages() || [], []);

  const handleImageClick = (amazonLink) => {
    if (amazonLink) {
      window.open(amazonLink, "_blank", "noopener,noreferrer");
    }
  };

  return (
    <div className="text-center">
      <h3>Final Suggestions</h3>
      <p>Pick your favorite gift idea:</p>
      <Row className="mt-3">
        {images.map((img, i) => (
          <Col key={i}>
            <Image
              src={getImageSrc(img.path)}
              thumbnail
              style={{ cursor: "pointer" }}
              onClick={() => handleImageClick(img.amazon_link)}
              title={`${img.name} - Click to view on Amazon`}
            />
            <div className="mt-2">
              <strong>{img.name}</strong>
              <p className="text-muted small">{img.description}</p>
            </div>
          </Col>
        ))}
      </Row>
    </div>
  );
}
