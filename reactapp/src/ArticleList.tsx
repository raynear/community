import React from "react";
//import { Fragment } from "react";
import gql from "graphql-tag";
import { useQuery } from "@apollo/react-hooks";
import { makeStyles, createStyles, Theme } from "@material-ui/core/styles";
import {
  Card /*, CardActions*/,
  CardContent /*, Button*/,
  Typography,
  Container,
  Grid
} from "@material-ui/core";

const GET_ARTICLES = gql`
  query {
    allArticle {
      subject
      contents
      commentmodelSet {
        comment
      }
    }
  }
`;

interface comment {
  id: "";
  comment: "";
}

interface article {
  id: "";
  subject: "";
  contents: "";
  commentmodelSet: Array<comment>;
}

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    card: {
      minWidth: 275
    },
    bullet: {
      display: "inline-block",
      margin: "0 2px",
      transform: "scale(0.8)"
    },
    title: {
      fontSize: 14
    },
    pos: {
      marginBottom: 12
    },
    formControl: {
      margin: theme.spacing(3)
    },
    container: {
      paddingTop: theme.spacing(4),
      paddingBottom: theme.spacing(4)
    }
  })
);

function ArticleList() {
  const classes = useStyles();
  const { loading, error, data } = useQuery(GET_ARTICLES);
  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error!:{error}</p>;
  return (
    <Container maxWidth="lg" className={classes.container}>
      <Grid container spacing={3}>
        {data.allArticle.map((item: article) => (
          <Grid item xs={12} md={12} lg={12}>
            <Card key={item.id} className={classes.card}>
              <CardContent>
                <Typography
                  className={classes.title}
                  color="textSecondary"
                  gutterBottom
                >
                  {" "}
                  Type Of Proposal
                </Typography>
                <Typography variant="h5" color="textPrimary" gutterBottom>
                  {item.subject}
                </Typography>
                <Typography variant="h6" color="textSecondary">
                  {item.contents}
                </Typography>

                {item.commentmodelSet.map((comment: comment) => (
                  <Card key={comment.comment} className={classes.card}>
                    <CardContent>
                      <Typography>{comment.comment}</Typography>
                    </CardContent>
                  </Card>
                ))}
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
}

export default ArticleList;
