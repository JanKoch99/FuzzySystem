import './App.css'
import {Container, Nav, Navbar} from "react-bootstrap";
import {Link, Routes, Route} from "react-router-dom";
import UserData from "./pages/UserData";
import OtherPersonData from "./pages/OtherPersonData";
import ImageChoice from "./pages/ImageChoice";
import FinalSuggestion from "./pages/FinalSuggestion";
import Home from "./pages/Home.jsx";

function App() {

  return (
    <div className="bg-dark min-vh-100 text-white">
        <Navbar bg="dark" variant="dark" expand="lg">
            <Container>
                <Navbar.Brand as={Link} to="/">GiftGenie App</Navbar.Brand>
                <Nav className="me-auto">
                    <Nav.Link as={Link} to="/user">Your Data</Nav.Link>
                    <Nav.Link as={Link} to="/other">Other Person</Nav.Link>
                </Nav>
            </Container>
        </Navbar>
        <Container className="mt-4">
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/user" element={<UserData />} />
                <Route path="/other" element={<OtherPersonData  />} />
                <Route path="/images" element={<ImageChoice  />} />
                <Route path="/suggestion" element={<FinalSuggestion  />} />
            </Routes>
        </Container>
    </div>
  )
}

export default App
